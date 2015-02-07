from django.db import models
from polymorphic import PolymorphicModel
from django.contrib.auth.models import User


'''This needs to go towards the top'''
class LegalEntity(models.Model):
	given_name = models.TextField(max_length=30)
	creation_date = models.DateField()
	address1 = models.TextField(max_length=50)
	address2 = models.TextField(max_length=50)
	city = models.TextField(max_length=20)
	state = models.CharField(max_length=2)
	zip = models.IntegerField(max_length=5)
	email = models.TextField(max_length=100)

'''Needs to go before InventoryImage'''
class Photograph(models.Model):
	image = models.ImageField()
	Date = models.DateField()
	Place = models.TextField(max_length=100)
	person_id = models.ForeignKey('Person')

'''Needs to go before Inventory'''
class InventoryImage(models.Model):
	caption = models.TextField(max_length=300)
	photograph_id = models.ForeignKey('Photograph')

'''This needs to go towards the top'''
class Inventory(PolymorphicModel):
	name = models.TextField(max_length=30)
	description = models.TextField(max_length=300)
	value = models.DecimalField(max_digits=10, decimal_places=2)
	inventory_image_id = models.ForeignKey('InventoryImage')
	legal_entity_id = models.ForeignKey('LegalEntity')

'''This needs to go towards the top'''
class Person(LegalEntity):
	family_name = models.TextField(max_length=30)
	user = models.OneToOneField(User)

'''This needs to go towards the top'''
class Product(Inventory):
	category = models.TextField(max_length=50)

'''This needs to go towards the top'''
class Item(Inventory):
	standard_rental_price = models.DecimalField(max_digits=10, decimal_places=2)

'''This needs to go towards the top'''
class Return(models.Model):
	return_time = models.DateTimeField()
	fees_paid = models.BooleanField()

class Organization(LegalEntity):
	organization_type = models.TextField(max_length=50)
	person_id = models.ForeignKey('Person')

class Phone(models.Model):
	extension = models.IntegerField(max_length=6)
	phone_type = models.TextField(max_length=50)
	legal_entity_id = models.ForeignKey('LegalEntity')


class BulkDetail(models.Model):
	quantity = models.IntegerField(max_length=10)
	price = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
	CARD_CHOICES =  (
			('v', 'Visa'),
			('a', 'American Express'),
			('m', 'Master Card'),
			('d', 'Discover Card')
		)
	card_name = models.TextField(max_length=100)
	card_type = models.CharField(max_length=1, choices=CARD_CHOICES, default='v')
	card_number = models.IntegerField(max_length=15)

class BulkProduct(Product):
	quantity = models.IntegerField(max_length=10)

class IndividualProduct(Product):
	date_made = models.DateField()
	order_id = models.ForeignKey('Order', null=True)

class PersonalProduct(Product):
	order_form_name = models.TextField(max_length=30)
	prodction_time = models.DateTimeField()

class PersonalDetail(models.Model):
	order_file = models.TextField(max_length=30)

class Event(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()

class Venue(models.Model):
	name = models.TextField(max_length=50)
	address = models.TextField(max_length=100)
	city = models.TextField(max_length=30)
	state = models.CharField(max_length=2)
	zip = models.IntegerField(max_length=5)
	email = models.TextField(max_length=100)
	event_id = models.ForeignKey('Event')

class EventType(models.Model):
	name = models.TextField(max_length=50)
	description = models.TextField(max_length=300)
	event_id = models.ForeignKey('LegalEntity', null=True)

class Agent(Person):
	appointment_date = models.DateTimeField()

class RentableItem(Item):
	is_rentable = models.BooleanField()

class WardrobeItem(Item):
	size = models.FloatField()
	size_modifier = models.TextField(max_length=100)
	gender = models.CharField(max_length=1)
	color = models.TextField(max_length=10)
	pattern = models.TextField(max_length=50)
	start_year = models.DateField()
	end_year = models.DateField()
	note = models.TextField(max_length=500)

class Order(models.Model):
	order_date = models.DateField()
	phone = models.IntegerField(max_length=15)
	date_packed = models.DateField()
	date_paid = models.DateField()
	date_shipped = models.DateField()
	tracking_number = models.IntegerField(max_length=50)
	agent_id = models.ForeignKey('Agent', null=True)

class Area(models.Model):
	name = models.TextField(max_length=50)
	description = models.TextField(max_length=300)
	place_number = models.IntegerField(max_length=4)
	agent_id = models.ForeignKey('Agent')
	event_id = models.ForeignKey('Event')

class RentedItem(models.Model):
	condition = models.TextField(max_length=500)
	new_damage = models.TextField(max_length=500)
	damage_fee = models.DecimalField(max_digits=10, decimal_places=2)
	late_fee = models.DecimalField(max_digits=10, decimal_places=2)
	return_id = models.ForeignKey('Return', null=True)

class SaleItem(models.Model):
	name = models.TextField(max_length=50)
	description = models.TextField(max_length=300)
	low_price = models.DecimalField(max_digits=10, decimal_places=2)
	high_price = models.DecimalField(max_digits=10, decimal_places=2)
	sale_item_id = models.ForeignKey('Area')

class InventoryPhotograph(models.Model):
	caption = models.TextField(max_length=300)

class BulkDetail(models.Model):
	quantity = models.IntegerField(max_length=6)
	price = models.DecimalField(max_digits=10, decimal_places=2)

class PersonalDetail(models.Model):
	order_file = models.FileField()
