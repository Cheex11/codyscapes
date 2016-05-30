# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-27 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20160524_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='location_string',
            field=models.CharField(default='dallas', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='purchase_link',
            field=models.CharField(default='link', max_length=200),
            preserve_default=False,
        ),
    ]