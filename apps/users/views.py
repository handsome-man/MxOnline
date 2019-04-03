from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View

# Create your views here.
from course.models import Course
from organization.models import CourseOrg
from users.forms import LoginForm, RegisterForm
from users.models import Banner
from users.utils import get_param


class IndexView(View):
    """首页"""

    @staticmethod
    def get(request):
        all_banners = Banner.objects.all().order_by('index')
        courses = Course.objects.filter(is_banner=False)[:6]
        banner_courses = Course.objects.filter(is_banner=True)[:2]
        course_organizations = CourseOrg.objects.all()[:15]
        return render(request, 'index.html', {'all_banners': all_banners,
                                              'courses': courses,
                                              'banner_course': banner_courses,
                                              'course_organizations': course_organizations})


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


class UserInfo(View):
    """用户中心"""
    @staticmethod

