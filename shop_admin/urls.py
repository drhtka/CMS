# -*- coding: utf-8 -*-

from django.urls import path

from shop_admin.views import CategoryList, IndexShopAdmin

app_name = 'shop_admin'

urlpatterns = [

    path('categorylist/', CategoryList, name='categorylist'),
    path('index_admin/', IndexShopAdmin, name='index_admin'),

    # path('<slug:product_slug>', views.product_detail, name='product_detail'),

    # path('<slug:product_slug>', views.product_detail,
    #      name='product_detail'),
    # path('<slug:category_slug>/<slug:product_slug>/', views.product_detail,
    #      name='product_detail'),
    # path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),


]
