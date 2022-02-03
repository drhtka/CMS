# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'create_page'

urlpatterns = [

    path('create_page/', views.create_page, name='create_page'),
    # path('<slug:product_slug>', views.product_detail, name='product_detail'),


    # path('<slug:product_slug>', views.product_detail,
    #      name='product_detail'),
    # path('<slug:category_slug>/<slug:product_slug>/', views.product_detail,
    #      name='product_detail'),
    # path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),


 ]
