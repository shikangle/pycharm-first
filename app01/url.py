#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 14:21
# @Auther  : Frank
# @Email   : 550862872@qq.com
# @File    : url.py
# @Software: PyCharm


"""untitled2 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

urlpatterns = [

    url(r'^Login/',views.login),
    url(r'^orm/',views.orm),
    url(r'^index/',views.index),
    url(r'^user_info/',views.user_info),
    url(r'^userdetail-(?P<nid>\d+)/',views.user_detail),
    url(r'^userdel-(?P<nid>\d+)/',views.user_del),
    url(r'^useredit-(?P<nid>\d+)/',views.user_edit),


]
