# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-30 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20160530_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_file',
            field=models.ImageField(height_field='height_field', upload_to='photos/media/', width_field='width_field'),
        ),
    ]
