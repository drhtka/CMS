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
    image = models.ImageField('Картинка', upload_to='brands/', blank=True, null=True,
                              default='user_default_profile.jpg', )

    def __str__(self):
        return self.name


class Promo(models.Model):
    class Meta:
        verbose_name = 'Реклама акции'
        verbose_name_plural = 'Реклама акции'

    slug = models.SlugField(max_length=64, unique=True)
    image = models.ImageField('Картинка', upload_to='promo/', blank=True, null=True,
                              default='user_default_profile.jpg', )
    promo_type = models.CharField('Тип рекламы', max_length=128)
    description = models.TextField('Описание', )
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
    image = models.ImageField('Картинка', upload_to='category/', blank=True, null=True,
                              default='user_default_profile.jpg', )

    # description = models.TextField('Описание')

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
    count = models.IntegerField('Количество')
    brand_name = models.ForeignKey(Brands, verbose_name='Бренд', on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE, default=None)
    promo = models.ManyToManyField(Promo, verbose_name='Реклама акции', )

    def __str__(self):
        return f'{self.brand_name} {self.model}'


class Notebook(Item):
    class Meta:
        verbose_name = 'Ноутбуки и ПК'
        verbose_name_plural = 'Ноутбуки и ПК'

    name = models.CharField('Название', max_length=128, blank=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    display = models.DecimalField('Экран', max_digits=3, decimal_places=1)
    memory = models.IntegerField('Оперативня память')
    video_memory = models.IntegerField('Видео память')
    cpu = models.CharField('Процессор', max_length=128)
    image = models.ImageField('Картинка', upload_to='notebook/', blank=True, null=True,
                              default='user_default_profile.jpg', )

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

    name = models.CharField('Название', max_length=128, blank=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    energy_saving_class = models.CharField('Энергопотребление', max_length=2, default='A+')
    power = models.IntegerField('Мощность', default=0)
    width = models.FloatField('Ширина')
    height = models.FloatField('Высота')
    image = models.ImageField('Картинка', upload_to='dishwasher/', blank=True, null=True,
                              default='user_default_profile.jpg', )


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

    name = models.CharField('Название', max_length=128, blank=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    noise_level = models.FloatField('Уровень шума')
    power = models.IntegerField('Мощность')
    width = models.FloatField('Ширина')
    height = models.FloatField('Высота')
    eco_engine = models.BooleanField('Двигатель', default=False)
    image = models.ImageField('Картинка', upload_to='vacuumcleaner/', blank=True, null=True,
                              default='user_default_profile.jpg', )

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

    name = models.CharField('Название', max_length=128, blank=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    display = models.DecimalField('Экран', max_digits=2, decimal_places=0)
    memory = models.IntegerField('Память')
    display_type = models.CharField('Разрешение', max_length=8)
    smart_tv = models.BooleanField('SmartTV', False)
    image = models.ImageField('Картинка', upload_to='tv/', blank=True, null=True, default='user_default_profile.jpg', )

    def colored_name(self):
        return format_html(
            '<span style="color: #0f2fff;">{} {}</span>',
            self.model,
            self.brand_name,
        )

class Clothes(Item):
    class Meta:
        verbose_name = 'Взрослая одежда'
        verbose_name_plural = 'Взрослая одежда'

    name = models.CharField('Название', max_length=128, blank=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    image = models.ImageField('Картинка', upload_to='clothes/', blank=True, null=True, default='user_default_profile.jpg', )

    def colored_name(self):
        return format_html(
            '<span style="color: #0f2fff;">{} {}</span>',
            self.model,
            self.brand_name,
        )

