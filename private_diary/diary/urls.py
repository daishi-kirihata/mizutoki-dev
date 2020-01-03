# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 04:48:17 2020

@author: hajime
"""


from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]