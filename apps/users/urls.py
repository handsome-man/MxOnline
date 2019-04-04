# -*- coding: utf-8 -*-
__author__ = 'kevin'
__date__ = '2019/4/4 16:30'

from django.urls import path

from .views import MyInfoView, MyFavCourseView, MyCourseView, \
    MyMessageView, MyFavTeacherView

urlpatterns = [
    path('mycenter', MyInfoView.as_view(), name='mycenter'),
    path('myfavcourse', MyFavCourseView.as_view(), name='myfavcourse'),
    path('mycourse', MyCourseView.as_view(), name='mycourse'),
    path('mymessage', MyMessageView.as_view(), name='mymessage'),
    path('mycourse_teacher', MyFavTeacherView.as_view(), name='mycourse_teacher'),
]
