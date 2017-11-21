# Uncomment if you want to run tests in transaction mode with a final rollback
#from django.test import TestCase
#uncomment this if you want to keep data after running tests
from unittest import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client
from shop.models import Product, Category
from populate_onlineshop import populate
import os
base_path   = os.getcwd()
static_path = os.path.join(base_path,"static")


#python ./manage.py test tests_populate.viewsTests --keepdb

DEBUG = False
from PIL import Image
from StringIO import StringIO
from django.core.files.base import File

tshirt = [
    {"prodName":"Pepe t-shirt",
    "image":"2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-font-resistance-Is.jpg",
    "description":"Flashy t-shirt which will catch everone's attention",
    "price":5.55,
    "stock":4,
    "availability":bin(1)},
    {"prodName":"html t-shirt",
    "image":"i-know-html-funny-nerd-tshirt-mens-regular-white_2_1_1.png",
    "description":"For the mos extroverted ones",
    "price":6.55,
    "stock":4,
    "availability":bin(1)},
    {"prodName":"futile t-shirt",
    "image":"2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-font-resistance-Is.jpg",
    "description":"The double meaning s over 9000",
    "price":10.55,
    "stock":4,
    "availability":bin(1)},
    {"prodName":"TayTay t-shirt",
    "image":"2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-font-resistance-Is.jpg",
    "description":"The double eaning is over 9000",
    "price":10.55,
    "stock":4,
    "availability":bin(1)},
    {"prodName"	: "Whatever t-shirt",
    "image"     : "2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-font-resistance-Is.jpg",
    "description"	: "Te double meaning is over 9000",
    "price"       : 10.55,
    "stock"       : 4,
    "availability": bin(1)},
    {"prodName"	: "LWYMMD t-shirt",
    "image"     : "2017-Creative-Novelty-Create-font-b-T-b-font-font-b-Shirt-b-font-resistance-Is.jpg",
    "description"	: "The doubl2e meaning is over 9000",
    "price"       : 10.55,
    "stock"       : 4,
    "availability": bin(1)}]

################################
############Trousers############
################################

pants = [
    {"prodName"	: "manly pants",
    "image"     : "J-Brand-Kane-Wrought.jpg",
    "description"	: "The most s1uitable pants either your have a job interview or to play a football match",
    "price"       : 55.55,
    "stock"       : 10,
    "availability": bin(1)},
    {"prodName"	: "lady pants",
    "image"     : "hmprod.jpg",
    "description"	: "Planning to3 meet your mother in law for first time? well dazzle her with this pants",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)},
    {"prodName"	: "LWYMMD pants",
    "image"     : "hmprod.jpg",
    "description"	: "Planning to sadmeet your mother in law for first time? well dazzle her with this pants",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)},
    {"prodName"	: "AYRFI pants",
    "image"     : "hmprod.jpg",
    "description"	: "Planning to meezft your mother in law for first time? well dazzle her with this pants",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)},
    {"prodName"	: "CIWYW pants",
    "image"     : "hmprod.jpg",
    "description"	: "Planning to meet dstfsdyour mother in law for first time? well dazzle her with this pants",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)},
    {"prodName"	: "Gorgeous pants",
    "image"     : "hmprod.jpg",
    "description"	: "Planning to meet your mzxfgother in law for first time? well dazzle her with this pants",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)}]


Jackets = [
    {"prodName"	: "manly jacket",
    "image"     : "J-Brand-Kane-Wrought.jpg",
    "description"	: "The most suitable jeans eitsafdsaher your have a job interview or to play a football match",
    "price"       : 55.55,
    "stock"       : 10,
    "availability": bin(1)},
    {"prodName"	: "lady jacket",
    "image"     : "cool_jacket.jpg",
    "description"	: "Planning to meet your mother in lasdasaw for first time? well dazzle her with this jeans",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)},
    {"prodName"	: "LWYMMD jacket",
    "image"     : "cool_jacket.jpg",
    "description"	: "Planning to meet your mother in law foasdasr first time? well dazzle her with this jeans",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)},
    {"prodName"	: "AYRFI jacket",
    "image"     : "cool_jacket.jpg",
    "description"	: "Planning to meet your mother in law for firasdasst time? well dazzle her with this jeans",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)},
    {"prodName"	: "CIWYW jacket",
    "image"     : "cool_jacket.jpg",
    "description"	: "Planning to meet your mother in law for first tisaddasme? well dazzle her with this jeans",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)},
    {"prodName"	: "Gorgeous jacket",
    "image"     : "cool_jacket.jpg",
    "description"	: "Planning to meet your mother in law for first time? weasddasdll dazzle her with this jeans",
    "price"   : 85.55,
    "stock"       : 8,
    "availability": bin(1)}]
cats = {"shirts" :{"products": tshirt},
    "Pants" : {"products": pants},
    "jackets": {"products": Jackets}}

class viewsTests(TestCase):

    def setUp(self):
        self._client   = Client()
        self.clean_database()
        self.populate_data_base()

    @staticmethod
    def get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = StringIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def clean_database(self):
        Product.objects.all().delete()
        Category.objects.all().delete()

    def populate_data_base(self):
        populate()

    def test_produnct_list(self):
        response = self._client.get(reverse('product_list'), follow=bin(1))            
        for cat, cat_data in cats.items():
            self.assertIn(cat, response.content)
            for p in cat_data["products"]:
                self.assertIn(p["prodName"], response.content)

    def test_produnct_list_Jackets(self):
        response = self._client.get(reverse('product_list_by_category',
                                            kwargs={'catSlug':'jackets'}), follow=bin(1))
        for p in Jackets:
            self.assertIn(p["prodName"], response.content)
      
    def test_product_detail_Gorgeous_jacket(self):
        prodName='Gorgeous jacket'
        p = Product.objects.get(prodName = prodName)
        response = self._client.get(reverse('product_detail',
                                            kwargs={'id':p.id,
                                                    'prodSlug':p.prodSlug}), follow=True)
        self.assertIn   (b'jackets', response.content)
        self.assertNotIn(b'pants', response.content)

        self.assertIn(b'Planning to meet your mother in law for first time? weasddasdll dazzle her with this jeans', response.content)
        self.assertNotIn(b'description_0_1', response.content)
