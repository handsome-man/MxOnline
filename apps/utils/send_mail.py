# -*- coding: utf-8 -*-
__author__ = 'kevin'
__date__ = '2019/4/6 23:10'

import base64
from datetime import datetime
from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_HOST_USER


def random_str(random_length=8):
    """生成随机字符串"""
    str = ''
    # 生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str

def send_register_email(email, email_send_type):
    """
    发邮箱激活用户
    :param email: 接受者邮箱
    :param email_send_type: 邮箱类型(注册、找回密码或者修改邮箱)
    :return: 无返回值
    """
    code = random_str(16)
    email_verify_record = EmailVerifyRecord()
    email_verify_record.email = email
    email_verify_record.send_type = email_send_type
    email_verify_record.send_time = datetime.now()
    email_verify_record.code = code
    email_verify_record.save()

    if email_send_type == 'register':
        subject = '在线学习网激活链接'
        message = '请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}'.format(code)
        """
        :param subject: 主题
        :param message: 内容
        :param from_email: 从那个邮箱发送
        :param recipient_list: 接收人列表
        """
        send_mail(subject, message, from_email=EMAIL_HOST_USER, recipient_list=[email])

