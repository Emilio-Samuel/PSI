# -*- coding: utf-8 -*-
import datetime

from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
	catName = models.CharField(max_length=128, unique=True)
	catSlug = models.SlugField(unique=True)
	def save(self, *args, **kwargs):
		self.catSlug = slugify(self.catName)
		super(Category,self).save(*args,**kwargs)

	def __str__(self):
		return self.catName
        
class Product(models.Model):
	category 	=  models.ForeignKey(Category, null = False)
	prodName	=  models.CharField(max_length=128, unique=True , null=False)
	prodSlug 	=  models.SlugField(unique=True)
	image    	=  models.ImageField(upload_to="images/products", blank=True, null=True)
	description	=  models.CharField(max_length=128, unique=True , null=False)
	price       =  models.FloatField(null = False, default = 0)
	stock       =  models.IntegerField(default=1, null = False)
	availability=  models.BinaryField(default = bin(1), null = False)
	created     =  models.DateTimeField(default = datetime.now())
	updated     =  models.DateTimeField(default = datetime.now())
	
	def save(self, *args, **kwargs):
		self.prodSlug = slugify(self.prodName)
		super(Product,self).save(*args,**kwargs)
	
	def __str__(self):
		return self.prodName
