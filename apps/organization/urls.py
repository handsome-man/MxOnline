# -*- coding: utf-8 -*-
__author__ = 'kevin'
__date__ = '2019/4/4 16:39'

from django.urls import path

from users.views import MyFavOrgView

urlpatterns = [
    path('myorg', MyFavOrgView.as_view(), name='myorg'),
]
