# Generated by Django 3.2 on 2021-05-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210509_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.AddField(
            model_name='order',
            name='order_placed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
