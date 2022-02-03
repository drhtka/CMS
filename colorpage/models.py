# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.urls import reverse
#
# class CreatedChildPage(models.Model):
#     """ckeitor"""
#     class Meta:
#         verbose_name = 'добавляем детеныша'
#         verbose_name_plural = 'добавляем детеныша'
#
#     name = models.CharField('Цвет ', max_length=128)
#     slug = models.SlugField(max_length=64, unique=True)
#     image = models.ImageField('Картинка', upload_to='createdchild/', blank=True, null=True,
#                               default='user_default_profile.jpg', )
#     style = models.CharField('CSS', max_length=128)



class ColorPages(models.Model):
    """создание странички"""
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Цвет странички'
        verbose_name_plural = 'Цвет странички'

    name = models.CharField('Цвет ', max_length=128)
    slug = models.SlugField(max_length=64, unique=True)
    image = models.ImageField('Картинка', upload_to='colorpages/', blank=True, null=True,
                              default='user_default_profile.jpg', )


    # description = models.TextField('Описание')

    def __str__(self):
        #return self.name
        return "Название: {} id: {}".format(self.name, self.pk)

    def get_absolute_url(self):
        return reverse(
            'colorpage:product_list_by_category',
            args=[self.slug]
        )

class ChangeColor(models.Model):

    color = models.ForeignKey(ColorPages, related_name = 'color', on_delete = models.CASCADE, verbose_name='Цвет')
    name = models.CharField('Название страницы', max_length=128, blank=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True)

    def __str__(self):
        #return self.name
        return "Название страницы: {} ".format(self.name)

    class Meta:
        verbose_name= 'Выбрать цвет'
        verbose_name_plural = 'Выбрать цвет'
