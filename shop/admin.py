# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import Category, Promo, Brands, Item, Dishwasher, Notebook, VacuumCleaner, TV, Clothes

#for model in [Clothes]:  # Dishwasher, Brand, TV
#    admin.site.register(model)


# @admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'get_img',)
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('name',)
    fields = ('name', 'slug', 'image', 'get_img',)
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'


admin.site.register(Brands, BrandsAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'get_img', 'id',)
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('name',)
    fields = ('name', 'slug', 'image', 'get_img',)
    readonly_fields = ('get_img',)


    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('slug', 'promo_type', 'get_img', 'start_time', 'end_time', 'id', 'available',)
    prepopulated_fields = {'slug': ('promo_type',)}
    list_editable = ('promo_type', 'start_time', 'end_time', 'available',)
    fields = ('promo_type', 'slug', 'image', 'start_time', 'end_time', 'get_img',)
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'

@admin.register(Dishwasher)
class DishwasherAdmin(admin.ModelAdmin):
    class Media:
        css = {}

    list_display = ('model', 'brand_name', 'price',
                    'colored_name', 'get_img',  'id', 'category', )#'test_show_promo',,
    list_filter = ('price', 'brand_name', 'color',)
    fieldsets = (
        ('Основная информация', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('brand_name', 'category', 'model', 'name', 'slug', 'image'),
        }),
        ('Расширеные опции', {
            'classes': ('wide', 'extrapretty'),
            'description': ('Описание полей'),
            'fields': ('price', 'color', 'energy_saving_class', 'power', 'width', 'height', 'promo', 'description', 'warranty', 'count'),
        }),)

    sortable_by = 'price', 'brand_name'
    search_fields = ['brand_name__pk']
    # exclude = ('price',)
    empty_value_display = '-Без бренда-'
    # readonly_fields = ['price']
    readonly_fields = ('get_img',)
    prepopulated_fields = {'slug': ('name',)}

    def test_show_promo(self, obj):  # используем объект который пердается в данную функцию
        return obj.promo  # и выводим то поле которое нам надо

    def delete_model(self, request, obj):
        pass

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="40px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'
    list_per_page = 10


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    class Media:
        css = {}

    list_display = ('model', 'brand_name', 'price',
                    'colored_name', 'get_img', 'id', 'category')
    list_filter = ('price', 'brand_name', 'color',)
    fieldsets = (
        ('Основная информация', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('brand_name', 'category', 'model', 'name', 'slug', 'image'),
        }),
        ('Расширеные опции', {
            'classes': ('wide', 'extrapretty'),
            'description': ('Описание полей'),
            'fields': ('price', 'color', 'display', 'memory', 'video_memory', 'cpu', 'description', 'warranty', 'count'),
        }),)

    sortable_by = 'price'
    search_fields = ['brand_name__pk']
    # exclude = ('price',)
    empty_value_display = '-Без бренда-'
    # readonly_fields = ['price']
    readonly_fields = ('get_img',)
    prepopulated_fields = {'slug': ('name',)}

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="40px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'
    list_per_page = 10


@admin.register(VacuumCleaner)
class VacuumCleanerAdmin(admin.ModelAdmin):
    class Media:
        css = {}

    list_display = ('model', 'brand_name', 'price',
                    'color', 'colored_name', 'get_img',  'id', 'category')
    list_filter = ('price', 'brand_name', 'color',)
    fieldsets = (
        ('Основная информация', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('brand_name', 'category', 'model', 'name', 'slug', 'image'),
        }),
        ('Расширеные опции', {
            'classes': ('wide', 'extrapretty'),
            'description': ('Описание полей'),
            'fields': ('price', 'color', 'noise_level', 'power', 'width', 'height', 'description', 'warranty', 'count', 'eco_engine'),
        }),)

    sortable_by = 'price'
    search_fields = ['brand_name__pk']
    # exclude = ('price',)
    empty_value_display = '-Без бренда-'
    # readonly_fields = ['price']
    readonly_fields = ('get_img',)
    prepopulated_fields = {'slug': ('name',)}

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="40px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'
    list_per_page = 10



@admin.register(TV)
class TVAdmin(admin.ModelAdmin):
    class Media:
        css = {}

    list_display = ('model', 'brand_name', 'price',
                    'color', 'colored_name', 'get_img',  'id',)
    list_filter = ('price', 'brand_name', 'color',)
    fieldsets = (
        ('Основная информация', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('brand_name', 'category', 'model', 'name', 'slug', 'image'),
        }),
        ('Расширеные опции', {
            'classes': ('wide', 'extrapretty'),
            'description': ('Описание полей'),
            'fields': ('price', 'color', 'display', 'memory', 'display_type', 'description', 'warranty', 'count', 'smart_tv'),
        }),)

    sortable_by = 'price'
    search_fields = ['brand_name__pk']
    # exclude = ('price',)
    empty_value_display = '-Без бренда-'
    # readonly_fields = ['price']
    readonly_fields = ('get_img',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="40px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['brand_name__pk', 'category_name']
    list_display = ('model', 'category', 'brand_name', 'price', 'id') #'color', 'colored_name','get_img',
    list_filter = ('price', 'brand_name', 'category',)
    list_per_page = 10

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('model', 'category', 'brand_name', 'price', 'id', 'get_img' ) #'color', 'colored_name','get_img',
    list_filter = ('price', 'brand_name', 'color',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10


    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="40px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'
    readonly_fields = ('get_img',)

