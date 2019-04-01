from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View


# Create your views here.
from users.forms import LoginForm, RegisterForm
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
        return render(request, 'login.html')

    @staticmethod
    def post(request):
        login_form = LoginForm(get_param(request))
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # 注册并且激活才可以登录
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'login.html', {'login_form': login_form})
            else:
                return render(request, 'login.html', {'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    """注册页面"""

    @staticmethod
    def get(request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    @staticmethod
    def post(request):
        register_form = RegisterForm(get_param(request))


class ForgetPWD(View):
    """忘记密码"""

    @staticmethod
    def get(request):
        return render(request, 'forgetpwd.html', {})

    @staticmethod
    def post(request):
        pass
