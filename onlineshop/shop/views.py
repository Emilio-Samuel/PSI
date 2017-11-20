#AUTHOR EMILIO ACED FUENTES, ROBERTO ALCOVER COUSO
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from shop.models import *
from django.http import Http404

def product_list(request, catSlug=None):
	#Your code goes here
	#queries that fill, category, categories and products


	if catSlug == None:
		category = None
		categories=Category.objects.all()
		products = Product.objects.all()
	else:
		category = Category.objects.get(catSlug = catSlug)
		products = Product.objects.filter(category = category)	
		categories = Category.objects.all()

	return render(request,'shop/list.html', {'category': category, 'categories':categories, 'products': products})


def detailProduct(request, id, prodSlug):
	#Your code goes here
	#query that returns a product with id=protId

	product = Product.objects.get(id=id,prodSlug=prodSlug)
	return render(request, 'shop/detail.html', {'product': product})
	

def index(request):
	category_list = Category.objects.all()
	product_list = Product.objects.all()
	context_dict ={'categories': category_list,'products': product_list}
	return render(request, 'shop/index.html', context_dict)

def base(request):
	return render(request, 'shop/base.html')
