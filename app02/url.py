#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 14:28
# @Auther  : Frank
# @Email   : 550862872@qq.com
# @File    : url.py
# @Software: PyCharm
from django.conf.urls import url,include
from django.contrib import admin
from app02 import views

urlpatterns = [

    url(r'Login/',views.login),

]
