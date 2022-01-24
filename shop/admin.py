from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import Category, Promo, Brands


# @admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'get_img',)
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('name',)
    fields = ('name', 'slug', 'image', 'get_img',)
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80px"')
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
            return mark_safe(f'<img src="{obj.image.url}" width="80px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('slug', 'promo_type', 'get_img', 'start_time', 'end_time', 'id', 'available',)
    prepopulated_fields = {'slug': ('promo_type',)}
    list_editable = ('promo_type',  'end_time', 'available',)
    fields = ('promo_type', 'slug', 'image', 'start_time', 'end_time', 'get_img',)
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'


