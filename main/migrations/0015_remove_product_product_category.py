# Generated by Django 4.0.2 on 2022-06-05 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210522_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
    ]