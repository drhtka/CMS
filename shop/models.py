# -*- coding: utf-8 -*-
from django.db import models

class Brands(models.Model):
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'

    name = models.CharField('Бренды', max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    image = models.ImageField('Картинка', upload_to='brands/')

    def __str__(self):
        return self.name


class Promo(models.Model):
    class Meta:
        verbose_name = 'Реклама акции'
        verbose_name_plural = 'Реклама акции'

    slug = models.SlugField(max_length=64, unique=True)
    image = models.ImageField('Картинка', upload_to='promo/')
    promo_type = models.CharField('Тип рекламы', max_length=128)
    description = models.TextField('Опсание', )
    start_time = models.DateField('Начало', auto_now_add=True)
    end_time = models.DateField('Конец', null=True)
    available = models.BooleanField('Активно', default=True)

    def __str__(self):
        return self.promo_type

class Category(models.Model):
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название', max_length=128)
    slug = models.SlugField(max_length=64, unique=True)
    image = models.ImageField('Картинка', upload_to='category/')

    def __str__(self):
        return self.name

class Item(models.Model):
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Все товары'
        verbose_name_plural = 'Все товары'

    description = models.TextField('Описание')
    model = models.CharField('Модель', max_length=128)
    price = models.FloatField('Цена')
    color = models.CharField(max_length=30)
    warranty = models.IntegerField()
    count = models.IntegerField()
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    promo = models.ManyToManyField(Promo)

    def __str__(self):
        return f'{self.brand_name} {self.model}'
