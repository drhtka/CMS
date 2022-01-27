# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'colorpage'

urlpatterns = [
    path('', views.changecolor, name='changecolor'),
#     path('<slug:category_slug>',views.product_list,
#          name='product_list_by_category'),
#     path('<slug:category_slug>/<slug:product_slug>/',views.product_detail,
#          name='product_detail'),

 ]
