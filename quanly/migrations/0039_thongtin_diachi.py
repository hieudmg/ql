# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0038_thongke'),
    ]

    operations = [
        migrations.AddField(
            model_name='thongtin',
            name='diaChi',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
