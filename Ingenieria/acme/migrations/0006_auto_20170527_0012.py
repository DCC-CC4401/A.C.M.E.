# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0005_auto_20170527_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='favVendAmb',
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='favVendAmb',
            field=models.ManyToManyField(blank=True, to='acme.VendedorAmbProfile'),
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='favVendFijo',
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='favVendFijo',
            field=models.ManyToManyField(blank=True, to='acme.VendedorFijoProfile'),
        ),
    ]