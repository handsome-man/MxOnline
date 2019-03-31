from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View


# Create your views here.
from users.forms import LoginForm
from users.utils import get_param


class IndexView(View):
    """首页"""

    @staticmethod
    def get(request):
        return render(request, 'index.html', {})


class LoginView(View):
    """登录页面"""

    @staticmethod
    def get(request):
        return render(request, 'login.html', {})

    @staticmethod
    def post(request):
        login_form = LoginForm(get_param(request))
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print({'username': username, 'password': password})
            user = authenticate(username=username, password=password)
            if user is not None:
                # 注册并且激活才可以登录
                if user.is_active:
                    login(request, user)
                    return HttpResponse(reverse('index'))
                else:
                    return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})
        else:
            return render(request, 'login.html')


class RegisterView(View):
    """注册页面"""

    @staticmethod
    def get(request):
        return render(request, 'register.html', {})

    @staticmethod
    def post(request):
        pass


class ForgetPWD(View):
    """忘记密码"""

    @staticmethod
    def get(request):
        return render(request, 'forgetpwd.html', {})

    @staticmethod
    def post(request):
        pass
