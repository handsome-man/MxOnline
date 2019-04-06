# -*- coding: utf-8 -*-
__author__ = 'kevin'
__date__ = '2019/4/4 16:38'

from django.urls import path

from .views import CourseListView, CourseDetailView

urlpatterns = [
    # 课程列表
    path('list', CourseListView.as_view(), name='list'),
    # 课程详情
    path('detail', CourseDetailView.as_view(), name='detail'),
]