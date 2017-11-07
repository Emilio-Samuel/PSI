import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'onlineshop.settings')
django.setup()
from shop.models import Category, Product

image1 = "2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-fon_2huuUS0.jpg"
image2 = "2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-fon_2huuUS0.jpg"
image3 = "2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-fon_2huuUS0.jpg"
image4 = "2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-fon_2huuUS0.jpg"
image5 = "2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-fon_2huuUS0.jpg"
image6 = "2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-fon_2huuUS0.jpg"


catNew = Category.objects.get_or_create(catName='deals')[0]
catNew.save()

catNew2 = Category.objects.get_or_create(catName='bargains')[0]
catNew2.save()


deal1 = Product.objects.get_or_create(category=catNew, prodName='deal 1', image=image1,stock = 7, description="cheap", price=1, availability= bin(1))[0]
deal1.save()
deal2 = Product.objects.get_or_create(category=catNew, prodName='deal 2', image=image2,stock = 7,  description = "cheap2", price = 2, availability =  bin(1))[0]
deal2.save()
deal3 = Product.objects.get_or_create(category=catNew, prodName='deal 3', image=image3,stock = 7,  description="cheap3", price=3, availability= bin(1))[0]
deal3.save()




bargain1 = Product.objects.get_or_create(category=catNew2, prodName='bargain 1',stock = 7,  image=image4, description="really cheap 1", price=1, availability= bin(1))[0]
bargain1.save()
bargain2 = Product.objects.get_or_create(category=catNew2, prodName='bargain 2',stock = 7,  image=image5, description="really cheap 2", price=2, availability= bin(1))[0]
bargain2.save()
bargain3 = Product.objects.get_or_create(category=catNew2, prodName='bargain 3',stock = 7,  image=image6, description="really cheap 3", price=3, availability= bin(1))[0]
bargain3.save()


products = Product.objects.filter(category=catNew2)
print(products)

cats = Product.objects.get(prodSlug='deal-1')
category = Category.objects.get(catName=cats.category)
print(category.catSlug)

cats2 = Product.objects.filter(prodSlug='oferta-10')
if not cats2.exists():
    print("Product named  'oferta-10' does not exist.")
