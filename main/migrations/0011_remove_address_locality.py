# Generated by Django 3.2 on 2021-05-22 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210521_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='locality',
        ),
    ]
