# -*- coding: utf-8 -*-

from django.urls import path

from api.views import ItemAll
from shop_admin.views import CategoryList, IndexShopAdmin

app_name = 'shop_api'

urlpatterns = [

    path('item_all/', ItemAll, name='item_all'),
    # path('index_admin/', IndexShopAdmin, name='index_admin'),

    # path('<slug:product_slug>', views.product_detail, name='product_detail'),

    # path('<slug:product_slug>', views.product_detail,
    #      name='product_detail'),
    # path('<slug:category_slug>/<slug:product_slug>/', views.product_detail,
    #      name='product_detail'),
    # path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),


]
