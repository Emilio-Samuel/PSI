from django.conf.urls import url
from shop import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^(?P<catSlug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
	url(r'^(?P<prodId>\d+)/(?P<prodSlug>[-\w]+)/$',views.detailProduct, name ='detailProduct'),
]
