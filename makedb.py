import os
os.environ["DJANGO_SETTINGS_MODULE"] = "test_dmp.settings"
import django
django.setup()
from django.db import connection
import subprocess
from django.contrib.auth.models import Group, Permission, ContentType

cursor = connection.cursor()

# ADD LINES TO CREATE USERS, PRODUCTS, AREAS, EVENTS, ETC...
from homepage import models as hmod
user1 = hmod.User()
user1.username = 'klonghurst'
user1.set_password('klonghurst')
user1.first_name = 'Kyle'
user1.last_name = 'Longhurst'
user1.address = '1234 N. Street'
user1.save()

user2 = hmod.User()
user2.username = 'tredding'
user2.set_password('tredding')
user2.first_name = 'Taylor'
user2.last_name = 'Redding'
user2.address = '123 N. Street'
user2.save()

user3 = hmod.User()
user3.username = 'jlakenan'
user3.set_password('jlakenan')
user3.first_name = 'Joshua'
user3.last_name = 'Lakenan'
user3.address = '123 the hood'
user3.save()

#Venue
venue1 = hmod.Venue()
venue1.name = 'Serra Park'
venue1.address = '123 North Street'
venue1.city = 'Hometown'
venue1.state = 'DC'
venue1.zip = 88888
venue1.email = 'serra@orem.org'
venue1.save()

#Photograph
photo1 = hmod.Photograph()
photo1.image = 'image.jpg'
photo1.Date = '1995-02-11'
photo1.Place = 'Scerra Park'
photo1.save()

#Inventory
inv1 = hmod.Inventory()
inv1.name = 'American Flag'
inv1.description = 'This is a 40 x 40 american flag'
inv1.value = '89.99'
inv1.save()

#SaleItem
si1 = hmod.SaleItem()
si1.name = 'Liberty Bell Replica'
si1.description = 'A small replica of the liberty bell. Complete with crack'
si1.low_price = '12.99'
si1.high_price = '25.99'
si1.save()

#Area
area1 = hmod.Area()
area1.name = 'Black Smith'
area1.description = 'Bellows and all. Set up to be an exact replica of a true blacksmiths'
area1.place_number = '2'
area1.save()


#Permissions
permission1 = Permission()
permission1.codename = 'Admin'
permission1.content_type = ContentType.objects.get(id=7)
permission1.name = 'Has Admin Privileges'
permission1.save()

permission2 = Permission()
permission2.codename = 'Manager'
permission2.content_type = ContentType.objects.get(id=7)
permission2.name = 'Has Manager Privileges'
permission2.save()

permission3 = Permission()
permission3.codename = 'Guest'
permission3.content_type = ContentType.objects.get(id=7)
permission3.name = 'Has Guest Privileges'
permission3.save()

#Groups
group1 = Group()
group1.name = 'Admin'
group1.save()
group1.permissions.add(permission1)
permission = Permission.objects.get(id=34)
group1.permissions.add(permission)
permission = Permission.objects.get(id=35)
group1.permissions.add(permission)
permission = Permission.objects.get(id=36)
group1.permissions.add(permission)

group2 = Group()
group2.name = 'Manager'
group2.save()
group2.permissions.add(permission2)
permission = Permission.objects.get(id=35)
group2.permissions.add(permission)
permission = Permission.objects.get(id=36)
group2.permissions.add(permission)

group3 = Group()
group3.name = 'Guest'
group3.save()
group3.permissions.add(permission3)
permission = Permission.objects.get(id=36)
group3.permissions.add(permission)

#Assigning Users to Groups
user = hmod.User.objects.get(id=1)
user.groups.add(group1)

user = hmod.User.objects.get(id=2)
user.groups.add(group2)

user = hmod.User.objects.get(id=3)
user.groups.add(group3)
