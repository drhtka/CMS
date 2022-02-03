# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe

from colorpage.models import ColorPages, ChangeColor


@admin.register(ColorPages)
class ColorPagesAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'get_img', 'id')
    list_editable = ('name',)
    fields = ('name', 'slug', 'image', 'get_img',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра',


@admin.register(ChangeColor)
class ChangeColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'id')
    prepopulated_fields = {'slug': ('name',)}

    # fieldsets = (
    #     ('Основная информация', {
    #         'classes': ('wide', 'extrapretty'),
    #         'fields': ('brand_name', 'category', 'model', 'name', 'slug', 'image'),
    #     }),
    #     ('Расширеные опции', {
    #         'classes': ('wide', 'extrapretty'),
    #         'description': ('Описание полей'),
    #         'fields': ('price', 'color', 'energy_saving_class', 'power', 'width', 'height', 'promo', 'description', 'warranty', 'count'),
    #     }),)