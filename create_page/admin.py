# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe

from create_page.models import CreatedChildPage,  TypePages, ChangePage, CreateTwo

@admin.register(CreatedChildPage)
@admin.register(CreateTwo)


@admin.register(TypePages)
class TypePagesAdmin(admin.ModelAdmin):
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


@admin.register(ChangePage)
class ChangePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_page', 'id')
    prepopulated_fields = {'slug': ('name',)}