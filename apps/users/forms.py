from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from users.models import UserProfile


class LoginForm(forms.Form):
    """登录验证"""
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


    def clean_username(self):
        """检测用户名"""
        username = self.cleaned_data['username']
        if not UserProfile.objects.filter(username=username).exists():
            raise forms.ValidationError(('账号(%(username)s) 没有注册，请先注册'), params={'username': username})
        return username

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