from django.db import models

# Create your models here.

# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.urls import reverse


class CreatedChildPage(models.Model):
    """ckeitor"""

    class Meta:
        verbose_name = 'добавляем детеныша'
        verbose_name_plural = 'добавляем детеныша'

    name = models.CharField('Название ', max_length=128)
    slug = models.SlugField(max_length=64, unique=True)
    image = models.ImageField('Картинка', upload_to='createdchild/', blank=True, null=True,
                              default='user_default_profile.jpg', )
    style = models.CharField('свойство CSS', max_length=128)
    description = models.TextField('Описание')

    def __str__(self):
        # return self.name
        return "Название: {} id: {}".format(self.name, self.pk)

class CreateTwo(CreatedChildPage):
    """ckeitor"""

    class Meta:
        verbose_name = 'добавляем детеныша2'
        verbose_name_plural = 'добавляем детеныша2'

    nametwo = models.CharField('Название ', max_length=128)
    slugtwo = models.SlugField(max_length=64, unique=True)
    imagetwo = models.ImageField('Картинка', upload_to='createdchildtwo/', blank=True, null=True,
                              default='user_default_profile.jpg', )




class TypePages(models.Model):
    """создание странички"""

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Тип странички'
        verbose_name_plural = 'Тип странички'

    name = models.CharField('Название ', max_length=128)
    slug = models.SlugField(max_length=64, unique=True)
    image = models.ImageField('Картинка', upload_to='type_page/', blank=True, null=True,
                              default='user_default_profile.jpg', )

    def __str__(self):
        # return self.name
        return "Название: {} id: {}".format(self.name, self.pk)

    def get_absolute_url(self):
        return reverse(
            'colorpage:product_list_by_category',
            args=[self.slug]
        )


class ChangePage(models.Model):
    type_page = models.ForeignKey(TypePages, related_name='type_page', on_delete=models.CASCADE,
                                  verbose_name='Тип странички')
    child_create = models.ManyToManyField(CreatedChildPage, verbose_name='детеныш')
    name = models.CharField('Название страницы', max_length=128, blank=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True)

    def __str__(self):
        # return self.name
        return "Название страницы: {} ".format(self.name)

    class Meta:
        verbose_name = 'Выбрать страницу'
        verbose_name_plural = 'Выбрать страницу'
