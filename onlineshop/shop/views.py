from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from shop.models import Product,Category
from django.http import Http404
def index(request):
	category_list = Category.objects.all()
	product_list = Product.objects.all()
	context_dict ={'categories': category_list,'products': product_list}
	return render(request, 'shop/index.html', context_dict)
def base(request):
	return render(request, 'shop/base.html')
