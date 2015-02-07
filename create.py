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
u1 = hmod.SiteUser()
u1.username = 'tredding'
u1.set_password = 'tredding'
u1.first_name = 'Taylor'
u1.last_name = 'Redding'
u1.address = '123 N. Street'
u1.save()

u2 = hmod.SiteUser()
u2.username = 'dduck'
u2.set_password = 'dduck'
u2.first_name = 'Donald'
u2.last_name = 'Duck'
u2.address = '123 N. Street'
u2.save()

u3 = hmod.SiteUser()
u3.username = 'hpotter'
u3.set_password = 'hpotter'
u3.first_name = 'Harry'
u3.last_name = 'Potter'
u3.address = '123 N. Street'
u3.save()

# This is area
a1 = hmod.Area()
a1.name = 'Blacksmith'
a1.description = 'Make fun horseshoes!'
a1.place_number = '1234'
a1.save()

a2 = hmod.Area()
a2.name = 'Candy Shop'
a2.description = 'Come taste some incredible candy!'
a2.place_number = '12'
a2.save()

# This is events
e1 = hmod.Event()
e1.event_name = 'Annual Event'
e1.start_date = '2014-01-01'
e1.end_date = '2014-01-30'
e1.description = 'This is our annual event.'
e1.save()

e2 = hmod.Event()
e2.event_name = 'Small Event'
e2.start_date = '2014-03-01'
e2.end_date = '2014-03-10'
e2.description = 'This is our small event.'
e2.save()

# This is inventory
i1 = hmod.Inventory()
i1.name = 'Staff'
i1.description = 'This is a staff'
i1.value = '12.99'
i1.save()

i2 = hmod.Inventory()
i2.name = 'Cane'
i2.description = 'This is a cane'
i2.value = '12.99'
i2.save()

o1 = hmod.Organization()
o1.given_name = 'Store A'
o1.creation_date = '1999-01-01'
o1.address1 = '123 Street'
o1.city = 'Provo'
o1.state = 'UT'
o1.zip_code = '89898'
o1.email = 'asdf@gmail.com'
o1.organization_type = 'Store'
o1.save()

o2 = hmod.Organization()
o2.given_name = 'Store B'
o2.creation_date = '1999-01-01'
o2.address1 = '124 Street'
o2.city = 'Provo'
o2.state = 'UT'
o2.zip_code = '89899'
o2.email = 'asd@gmail.com'
o2.organization_type = 'Store'
o2.save()

v1 = hmod.Venue()
v1.venue_name = 'Rock Canyon Park'
v1.address = '12345 Street'
v1.city = 'Provo'
v1.state = 'UT'
v1.zip_code = '76457'
v1.email = 'jkdf@gmail.com'
v1.save()

v2 = hmod.Venue()
v2.venue_name = 'Parking lot'
v2.address = '1455 Street'
v2.city = 'Provo'
v2.state = 'UT'
v2.zip_code = '73357'
v2.email = 'parkhere@gmail.com'
v2.save()

# os.system(['python3', 'manage.py', 'migrate'])


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

group1 = Group()
group1.name = 'Admin'
group1.save()
group1.permissions.add(permission1)
permission = Permission.objects.get(id=97)
group1.permissions.add(permission)

group2 = Group()
group2.name = 'Manager'
group2.save()
group2.permissions.add(permission2)
permission = Permission.objects.get(id=98)
group1.permissions.add(permission)

group3 = Group()
group3.name = 'Guest'
group3.save()
group3.permissions.add(permission3)
permission = Permission.objects.get(id=99)
group1.permissions.add(permission)

user = hmod.SiteUser.objects.get(id=1)
user.groups.add(group1)

user = hmod.SiteUser.objects.get(id=2)
user.groups.add(group2)

user = hmod.SiteUser.objects.get(id=3)
user.groups.add(group3)
