# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-13 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tannersapp', '0003_musician_band'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='band',
        ),
        migrations.AddField(
            model_name='musician',
            name='band',
            field=models.ManyToManyField(to='tannersapp.Band'),
        ),
    ]