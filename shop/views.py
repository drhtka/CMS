# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.template.loader import render_to_string

import colorpage
from shop.models import Category, Item, Notebook, Dishwasher, VacuumCleaner, TV, Clothes
from colorpage.models import ColorPages, ChangeColor



# def product_detail(request, pk):#
#     print('product_detail')
#     print(pk)
#     sub_category = []
#     product = []

    # выводим подкатегории
    # category = Category.objects.filter(slug=category_slug).values('id')

    # categories_id = Category.objects.filter().values('id')
    # for categories_id_s in categories_id:
    #     print('categories_id')
    #     print(categories_id_s['id'])
    #     sample = categories_id_s['id']
    # category = get_object_or_404(Category, slug=category_slug)

    # product = get_object_or_404(Notebook, pk=pk)#category_id=category.id,

    # notebooks = Notebook.objects.filter(slug=product_slug).values()#category_id=category.id,

    # vacuumcleaners = VacuumCleaner.objects.filter().values()
    # televvisions = TV.objects.filter().values()
    # clotheses = Clothes.objects.filter().values()
    # dishwashers = Dishwasher.objects.filter().values()
    # for sub_categorys in notebooks:  # , vacuumcleaners, televvisions, clotheses, dishwashers:
    #     for tmpsub_category in sub_categorys:
    #         product.append(tmpsub_category)

    # return render(request, "colorpages/detail.html", {'product': product})