import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'onlineshop.settings')

import django
django.setup()
from shop.models import Category, Product
from django.core.files import File

def populate():
   # First, we will create lists of dictionaries containing the products
   # we want to add into each category.
   # Then we will create a dictionary of dictionaries for our categories.
   # This might seem a little bit confusing, but it allows us to iterate
   # through each data structure, and add the data to our models.



################################
############T-shirts############
################################
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

	###############################
	#########CATS##################
	###############################

	cats = {"shirts" :{"products": tshirt},
			"Pants" : {"products": pants},
			"jackets": {"products": Jackets}}
			
	###ADD CATEGORIES AND PAGES####

	for cat, cat_data in cats.items():
		c = add_cat(cat)
		for p in cat_data["products"]:
			add_prod(c, p["prodName"], p["image"],p["description"],p["price"],p["stock"],p["availability"])

	# Print out the categories we have added.
	for c in Category.objects.all():
		for p in Product.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_prod(cat, prodName, image, description, price, stock, availability):
	p = Product.objects.get_or_create(category=cat, prodName=prodName,description = description, price=price,stock = stock,availability = availability)[0]
	imageObject = File(open(os.path.join("images",image),'r'))
	p.image.save(image,imageObject,save = True)
	p.save()
	return p

def add_cat(name):
	c = Category.objects.get_or_create(catName=name)[0]
	c.catSlug = name
	c.save()
	return c

# Start execution here!
if __name__ == '__main__':
	print("Starting onlineshop population script...")
	populate()












