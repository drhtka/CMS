# -*- coding: utf-8 -*-
from django.db import models
from django.utils.html import format_html


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
    description = models.TextField('Опсание',)
    start_time = models.DateField('Начало', null=True)
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
        verbose_name = 'Все товары'
        verbose_name_plural = 'Все товары'

    description = models.TextField('Описание')
    model = models.CharField('Модель', max_length=128)
    price = models.FloatField('Цена')
    color = models.CharField('Цвет', max_length=30)
    warranty = models.IntegerField('Гарантия')
    count = models.IntegerField('Цена')
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    promo = models.ManyToManyField(Promo)

    def __str__(self):
        return f'{self.brand_name} {self.model}'

class Notebook(Item):
    class Meta:
        verbose_name = 'Ноутбуки'
        verbose_name_plural = 'Ноутбуки'

    display = models.DecimalField('Экран', max_digits=5, decimal_places=4)
    memory = models.IntegerField('Оперативня память')
    video_memory = models.IntegerField('Видео память')
    cpu = models.CharField('Процессор', max_length=128)

    def colored_name(self):
        return format_html(
            '<span style="color: #0fabff;">{} {}</span>',
            self.model,
            self.brand_name,
        )



class Dishwasher(Item):
    class Meta:
        verbose_name = 'Стиральные машины'
        verbose_name_plural = 'Стиральные машины'

    energy_saving_class = models.CharField(max_length=2, default='A+')
    power = models.IntegerField('Мощность', default=0)
    width = models.FloatField('Ширина')
    height = models.FloatField('Высота')

    def colored_name(self):
        return format_html(
            '<span style="color: #0fff47;">{} {}</span>',
            self.model,
            self.brand_name,
        )

class VacuumCleaner(Item):
    class Meta:
        verbose_name = 'Пылесосы'
        verbose_name_plural = 'Пылесосы'

    noise_level = models.FloatField('Уровень шума')
    power = models.IntegerField('Мощность')
    width = models.FloatField('Ширина')
    height = models.FloatField('Высота')
    eco_engine = models.BooleanField('Двигатель', default=False)

    def colored_name(self):
        return format_html(
            '<span style="color: #ff0FFF;">{} {}</span>',
            self.model,
            self.brand_name,
        )


class TV(Item):
    class Meta:
        verbose_name = 'Телевизоры'
        verbose_name_plural = 'Телевизоры'

    display = models.DecimalField('Экран', max_digits=5, decimal_places=4)
    memory = models.IntegerField('Память')
    display_type = models.CharField('Экран', max_length=8)
    smart_tv = models.BooleanField(False)

    def colored_name(self):
        return format_html(
            '<span style="color: #0f2fff;">{} {}</span>',
            self.model,
            self.brand_name,
        )
