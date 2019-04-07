"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

import xadmin
from users.views import IndexView, LoginView, RegisterView, ForgetPWD, LogoutView, UserActiveView
from MxOnline.settings import MEDIA_ROOT
from users import urls as user_url
from course import urls as course_url
from organization import urls as organization_url

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    re_path('active/(?P<active_code>.*)', UserActiveView.as_view(), name='active'),
    # 这是生成验证码的图片
    path('captcha/',include('captcha.urls')),
    path('forgetpwd', ForgetPWD.as_view(), name='forgetpwd'),

    # 用户路径
    path("users/", include((user_url, 'users'), namespace="users")),

    # 课程
    path("course/", include((course_url, 'course'), namespace="course")),

    # 组织机构
    path("organization/", include((organization_url, 'organization'), namespace="organization")),
]
