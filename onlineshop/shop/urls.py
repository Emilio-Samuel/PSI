from django.conf.urls import url
from shop import views
from django.conf import settings
from django.conf.urls.static import static
from shop.views import *

urlpatterns = [
	url(r'^$',views.product_list,name='product_list'),
	url(r'^(?P<catSlug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
	url(r'^(?P<id>\d+)/(?P<prodSlug>[-\w]+)/$',views.detailProduct, name ='product_detail'),
]
