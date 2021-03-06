# Generated by Django 3.2 on 2022-01-24 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishwasher',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.item')),
                ('energy_saving_class', models.CharField(default='A+', max_length=2)),
                ('power', models.IntegerField(default=0, verbose_name='Мощность')),
                ('width', models.FloatField(verbose_name='Ширина')),
                ('height', models.FloatField(verbose_name='Высота')),
            ],
            options={
                'verbose_name': 'Стиральные машины',
                'verbose_name_plural': 'Стиральные машины',
            },
            bases=('shop.item',),
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.item')),
                ('display', models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Экран')),
                ('memory', models.IntegerField(verbose_name='Оперативня память')),
                ('video_memory', models.IntegerField(verbose_name='Видео память')),
                ('cpu', models.CharField(max_length=128, verbose_name='Процессор')),
            ],
            options={
                'verbose_name': 'Ноутбуки',
                'verbose_name_plural': 'Ноутбуки',
            },
            bases=('shop.item',),
        ),
        migrations.CreateModel(
            name='TV',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.item')),
                ('display', models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Экран')),
                ('memory', models.IntegerField(verbose_name='Память')),
                ('display_type', models.CharField(max_length=8, verbose_name='Экран')),
                ('smart_tv', models.BooleanField(verbose_name=False)),
            ],
            options={
                'verbose_name': 'Телевизоры',
                'verbose_name_plural': 'Телевизоры',
            },
            bases=('shop.item',),
        ),
        migrations.CreateModel(
            name='VacuumCleaner',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.item')),
                ('noise_level', models.FloatField(verbose_name='Уровень шума')),
                ('power', models.IntegerField(verbose_name='Мощность')),
                ('width', models.FloatField(verbose_name='Ширина')),
                ('height', models.FloatField(verbose_name='Высота')),
                ('eco_engine', models.BooleanField(default=False, verbose_name='Двигатель')),
            ],
            options={
                'verbose_name': 'Пылесосы',
                'verbose_name_plural': 'Пылесосы',
            },
            bases=('shop.item',),
        ),
    ]
