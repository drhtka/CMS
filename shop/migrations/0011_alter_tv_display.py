# Generated by Django 3.2 on 2022-01-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_notebook_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tv',
            name='display',
            field=models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Экран'),
        ),
    ]
