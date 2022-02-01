# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'colorpage'

urlpatterns = [


    path('', views.changecolor, name='changecolor'),
    # path('<slug:product_slug>', views.product_detail, name='product_detail'),

    path('<int:pk>', views.product_detail, name='product_detail'),

    path('<slug:category_slug>', views.changecolor,
         name='product_list_by_category'),
    path('<str:sub_category>', views.sub_category, name='sub_category'),

    # path('<slug:product_slug>', views.product_detail,
    #      name='product_detail'),
    # path('<slug:category_slug>/<slug:product_slug>/', views.product_detail,
    #      name='product_detail'),
    # path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),


 ]
