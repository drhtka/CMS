from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.template.loader import render_to_string

import colorpage
from shop.models import Category, Item, Notebook, Dishwasher, VacuumCleaner, TV, Clothes
from colorpage.models import ColorPages, ChangeColor


def changecolor(request, category_slug=None):
    """"""

    global sample
    product = ''
    sub_category = []
    class_name_append = []
    class_name_append_s = []
    apend_name = []

    # вывожу имена классов в шабон для подкатегории
    list1 = Notebook, Dishwasher, VacuumCleaner, TV, Clothes
    list2 = Notebook.__name__, Dishwasher.__name__, VacuumCleaner.__name__, TV.__name__, Clothes.__name__
    # for verb_name in Notebook, Dishwasher, VacuumCleaner, TV, Clothes:
    #     # verb_name = {'verb__names': class_name_append }
    #     class_name_append.append(verb_name)
    #     print('class_name_append')
    # print('verb_name')
    # print(verb_name)
    for class_names in Notebook.__name__, Dishwasher.__name__, VacuumCleaner.__name__, TV.__name__, Clothes.__name__:
        # class_name = {'class_names': class_names}
        # print('class_name_append')
        apend_name.append(class_names)
        tmp_clas = class_name_append + apend_name
        # print('apend_name')
        # print(class_names)

    # print Notebook.compile.__module__
    # print(Notebook.__name__)

    # выводим все товары подкатегорий которые привязаны в категорию по слагу
    categories_id = Category.objects.filter(slug=category_slug).values('id', 'name')
    for categories_id_s in categories_id:
        # print('name')
        # print(categories_id_s['name'])
        sample = categories_id_s['id']
        notebooks = Notebook.objects.filter(category_id=sample).values()
        vacuumcleaners = VacuumCleaner.objects.filter(category_id=sample).values()
        televvisions = TV.objects.filter(category_id=sample).values()
        clotheses = Clothes.objects.filter(category_id=sample).values()
        dishwashers = Dishwasher.objects.filter(category_id=sample).values()
        for sub_categorys in notebooks, vacuumcleaners, televvisions, clotheses, dishwashers:
            for tmpsub_category in sub_categorys:
                sub_category.append(tmpsub_category)
        print('sub_category')
        # print(sub_category)

    products = []
    changecolor = ChangeColor.objects.filter().values()# меняем цвет швблона
    categories = Category.objects.all()
    # requested_category = get_object_or_404(Category, slug=category_slug)
    # products = Item.objects.filter(category=requested_category)
    if category_slug:
        """выводим товары по слагу каегории"""
        requested_category = Category.objects.filter(slug=category_slug).values('id')
        for requested_category in requested_category:
            if category_slug == 'kompyutery':
                verb_name = Notebook#, Dishwasher, VacuumCleaner, TV, Clothes:
                class_name_append.append(verb_name)
                notebooks = Notebook.objects.filter(category_id=requested_category['id']).values()  # Ноутбуки и ПК
                for notebook in notebooks:
                    products.append(notebook)
                    # print(notebooks)
            if category_slug == 'tehnika-dlya-doma':
                for verb_name in Dishwasher, VacuumCleaner: #, , TV, Clothes:
                    class_name_append.append(verb_name)
                vacuumcleaners = VacuumCleaner.objects.filter(category_id=requested_category['id']).values()  # Пылесосы
                dishwashers = Dishwasher.objects.filter(category_id=requested_category['id']).values()  # Стиральные машины
                for vacuumcleaner in vacuumcleaners:
                    products.append(vacuumcleaner)
                for dishwasher in dishwashers:  # , dishwashers
                    products.append(dishwasher)
            if category_slug == 'televizoryekrany':
                verb_name = TV#, Notebook, Dishwasher, VacuumCleaner, TV, Clothes:
                class_name_append.append(verb_name)
                televvisions = TV.objects.filter(category_id=requested_category['id']).values()  # Телевизоры
                for televvision in televvisions:
                    products.append(televvision)
            if category_slug == 'odezhda':
                verb_name = Clothes#, Notebook, Dishwasher, VacuumCleaner, TV:
                class_name_append.append(verb_name)
                clotheses = Clothes.objects.filter(category_id=requested_category['id']).values()  # Взрослая одежда
                for clothes in clotheses:
                    products.append(clothes)
                # if category_slug == 'tehnika-dlya-kuhni':
                #     dishwashers = Dishwasher.objects.filter(item_ptr_id=item['id']).values()
                #     for dishwasher in dishwashers:
                #         products.append(dishwasher)

    else:
        requested_category = None
        notebooks = Notebook.objects.filter().values()
        vacuumcleaners = VacuumCleaner.objects.filter().values()
        televvisions = TV.objects.filter().values()
        clotheses = Clothes.objects.filter().values()
        dishwashers = Dishwasher.objects.filter().values()
        for tmpprods in notebooks, vacuumcleaners, televvisions, clotheses, dishwashers:
            for tmpprod in tmpprods:
                products.append(tmpprod)

    for changecolors in changecolor:
        if changecolors['color_id'] == 2:
            print('белый')
            # for product in products:
            #     print('product')
            #     print(product)

            # template_name = 'black.html'
            return render(request, "colorpages/indextwoo.html",
                          {'categories': categories, 'requested_category': requested_category,
                           'products': products, 'class_name_append': class_name_append,
                           'class_name_append_s': class_name_append_s,
                           'apend_name': apend_name,
                           })
        if changecolors['color_id'] == 1:
            print('черный')
            return render(request, "colorpages/indexthree.html",
                          {'categories': categories, 'requested_category': requested_category, 'products': products})

    # if changecolor[0]['color_id'] == '2':
    #     print('2')
    #     template_name = 'white.html'

    # return render(request, "colorpages/" + template_name,)

    # return render(request, 'colorpages/white.html', )


def product_detail(request, pk):  # category_slug, product_slug
    print('product_detail')
    # print(category_slug, product_slug)
    print(pk)
    sub_category = []
    product = []
    # выводим товар при нажатии подкатегории

    # category = Category.objects.filter(slug=category_slug).values('id')

    # categories_id = Category.objects.filter().values('id')
    # for categories_id_s in categories_id:
    #     print('categories_id')
    #     print(categories_id_s['id'])
    #     sample = categories_id_s['id']
    # product = get_object_or_404(Notebook, pk=pk)#category_id=category.id, slug=product_slug
    # category = get_object_or_404(Category, slug=category_slug)
    # product = get_object_or_404(Notebook, slug=product_slug)#category_id=category.id,

    notebooks = Notebook.objects.filter(pk=pk).values()  # category_id=category.id,
    vacuumcleaners = VacuumCleaner.objects.filter(pk=pk).values()
    televvisions = TV.objects.filter(pk=pk).values()
    clotheses = Clothes.objects.filter(pk=pk).values()
    dishwashers = Dishwasher.objects.filter(pk=pk).values()

    for sub_categorys in notebooks, vacuumcleaners, televvisions, clotheses, dishwashers:  # ,
        for tmpsub_category in sub_categorys:
            product.append(tmpsub_category)
    # print('product')
    # print(product)

    return render(request, "colorpages/detail.html", {'product': product})


""""""


def sub_category(request, sub_category):
    print('test')
    print(sub_category)
    products = []
    sub_category_verbose_name = ''

    # выводим все товары подкатегории
    if sub_category == 'Ноутбуки и ПК':
        print('1')
        sub_category_verbose_name=sub_category
        notebooks = Notebook.objects.filter().values()
        for notebook in notebooks:
            products.append(notebook)

    if sub_category == 'Пылесосы':
        print('2')
        sub_category_verbose_name=sub_category
        vacuumcleaners = VacuumCleaner.objects.filter().values()
        for vacuumcleaner in vacuumcleaners:  # , dishwashers
            products.append(vacuumcleaner)

    if sub_category == 'Стиральные машины':
        print('3')
        sub_category_verbose_name=sub_category
        dishwashers = Dishwasher.objects.filter().values()
        for dishwasher in dishwashers:
            products.append(dishwasher)

    if sub_category == 'Телевизоры':
        print('4')
        sub_category_verbose_name=sub_category
        televvisions = TV.objects.filter().values()
        for televvision in televvisions:
            products.append(televvision)
    # ТЕМПЛЕЙТАМИ
    if sub_category == 'Взрослая одежда':
        print('5')
        sub_category_verbose_name=sub_category
        clotheses = Clothes.objects.filter().values()
        for clothes in clotheses:
            products.append(clothes)

                        # for sub_categorys in notebooks, vacuumcleaners, televvisions, clotheses, dishwashers:
                        #     for tmpsub_category in sub_categorys:
    #                     #         products.append(sub_categorys)
    # print('products')
    # print(products)

    # return redirect(
    #     'colorpage:changecolor',
    #     category_slug=category_slug, product_slug=product_slug)

    return render(request, "colorpages/indextwoo.html", {'products': products,
                                                         'sub_category_verbose_name': sub_category_verbose_name})


"""
    notebooks = Notebook.objects.filter().values()
    vacuumcleaners = VacuumCleaner.objects.filter().values()
    televvisions = TV.objects.filter().values()
    clotheses = Clothes.objects.filter().values()
    dishwashers = Dishwasher.objects.filter().values()
    for sub_categorys in notebooks, vacuumcleaners, televvisions, clotheses, dishwashers:
        for tmpsub_category in sub_categorys:
            sub_category.append(tmpsub_category)
"""
