# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.BinaryField(default=b'0b1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 18, 33, 14, 264767)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 18, 33, 14, 264799)),
        ),
    ]
