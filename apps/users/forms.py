from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from users.models import UserProfile


class UserCheckMixin(forms.Form):
    """用户名验证"""
    username = forms.CharField(required=True)

    def clean_username(self):
        """检测用户名"""
        username = self.cleaned_data['username']
        if not UserProfile.objects.filter(username=username).exists():
            raise forms.ValidationError(('账号(%(username)s) 没有注册，请先注册'), params={'username': username})
        return username


class EmailCheckMixin(forms.Form):
    """邮箱验证"""
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError(('邮箱(%(email)s))已经注册'), params={'email': email})


class LoginForm(UserCheckMixin):
    """登录验证"""
    password = forms.CharField(required=True, min_length=5)

    def clean(self):
        """检测密码"""
        if self.errors:
            return
        username = self.cleaned_data['username']
        user = authenticate(
            username=username,
            password=self.cleaned_data['password']
        )
        if user is None:
            raise forms.ValidationError('密码输入错误')


class RegisterForm(EmailCheckMixin):
    """注册表单"""
    password = forms.CharField(required=True, min_length=5)

    # captcha = CaptchaField(error_messages={'invalid': '验证码错误'})
    def save(self, commit=True):
        user = UserProfile.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        self.instance.user = user
        return super(RegisterForm, self).save(commit)
