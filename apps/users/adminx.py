# -*- coding: utf-8 -*-
__author__ = 'kevin'
__date__ = '2019/3/16 13:10'

from users.models import EmailVerifyRecord, Banner

import xadmin
from xadmin import views

class BaseSetting(object):
    '创建xadmin管理配置'

    # 开启主题功能
    use_bootswatch = True
    enable_themes = True


class GlobalSetting(object):
    '修改xadmin全局变量'

    # 修改title
    site_title = '后台管理系统'
    # 修改footer
    site_footer = '在线学习网'
    # 收起菜单
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    '注册EmailVerifyRecord模型'

    # 列表显示的字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 可以搜索的字段
    search_fields = ['code', 'email', 'send_type']
    # 筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    '注册Banner模型'
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

# 注册全局变量
xadmin.site.register(views.CommAdminView, GlobalSetting)

# 开启主题功能注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
