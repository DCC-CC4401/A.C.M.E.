# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedorfijoprofile',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='vendedorfijoprofile',
            name='init_time',
            field=models.TimeField(),
        ),
    ]