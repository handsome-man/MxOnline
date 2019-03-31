from django import forms


class LoginForm(forms.Form):
    """登录验证"""
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
