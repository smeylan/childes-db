# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-04 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0039_auto_20180404_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='clitic',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
