# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catName', models.CharField(unique=True, max_length=128)),
                ('catSlug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prodName', models.CharField(unique=True, max_length=128)),
                ('prodSlug', models.SlugField(unique=True)),
                ('image', models.ImageField(null=True, upload_to=b'../media/images/products', blank=True)),
                ('description', models.CharField(unique=True, max_length=128)),
                ('price', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=1)),
                ('availability', models.BinaryField(default=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 10, 29, 18, 38, 9, 188475))),
                ('updated', models.DateTimeField(default=datetime.datetime(2017, 10, 29, 18, 38, 9, 188506))),
                ('category', models.ForeignKey(to='shop.Category')),
            ],
        ),
    ]
