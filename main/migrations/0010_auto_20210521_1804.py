# Generated by Django 3.2 on 2021-05-21 18:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210509_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='email',
            field=models.EmailField(default='flagthis@localhost.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='fname',
            field=models.CharField(default='flagme@localhost', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='lname',
            field=models.CharField(default='flagme@localhost', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.PositiveBigIntegerField(default=1000000000, validators=[django.core.validators.MinValueValidator(1000000000)]),
            preserve_default=False,
        ),
    ]
