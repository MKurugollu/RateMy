# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratemy', '0005_auto_20180320_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(default='', upload_to='category_images'),
            preserve_default=False,
        ),
    ]
