# -*- coding: utf-8 -*-
__author__ = 'kevin'
__date__ = '2019/4/4 16:39'

from django.urls import path

from users.views import MyFavOrgView
from .views import TeacherListView, OrganizationList

urlpatterns = [
    # 我的组织
    path('myorg', MyFavOrgView.as_view(), name='myorg'),
    # 教师列表
    path('teacher_list', TeacherListView.as_view(), name='teacher_list'),
    # 组织列表
    path('org_list', OrganizationList.as_view(), name='org_list')
]
