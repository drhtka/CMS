# Generated by Django 3.2 on 2022-01-28 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colorpage', '0004_changecolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='changecolor',
            name='name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Цвет '),
        ),
        migrations.AddField(
            model_name='changecolor',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='changecolor',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='colorpage.colorpages', verbose_name='Цвет'),
        ),
    ]