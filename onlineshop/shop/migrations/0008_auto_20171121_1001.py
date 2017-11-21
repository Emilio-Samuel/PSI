# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20171120_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 21, 10, 1, 53, 134603)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 21, 10, 1, 53, 134632)),
        ),
    ]
