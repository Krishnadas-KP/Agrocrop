# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_farmerdetails_ac_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerdetails',
            name='Bank',
            field=models.CharField(default='XYZ BANK', max_length=15),
            preserve_default=False,
        ),
    ]
