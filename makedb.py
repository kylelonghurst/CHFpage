import os
os.environ["DJANGO_SETTINGS_MODULE"] = "test_dmp.settings"
import django
django.setup()
from django.db import connection
import subprocess

cursor = connection.cursor()

# ADD LINES TO CREATE USERS, PRODUCTS, AREAS, EVENTS, ETC...
from homepage import models as hmod
u1 = hmod.User()
u1.username = 'klonghurst'
u1.set_password = 'klonghurst'
u1.first_name = 'Kyle'
u1.last_name = 'Longhurst'
u1.address = '1234 N. Street'
u1.save()

u2 = hmod.User()
u2.username = 'dduck'
u2.set_password = 'dduck'
u2.first_name = 'Donald'
u2.last_name = 'Duck'
u2.address = '123 N. Street'
u2.save()

u3 = hmod.User()
u3.username = 'hpotter'
u3.set_password = 'hpotter'
u3.first_name = 'Harry'
u3.last_name = 'Potter'
u3.address = '123 N. Street'
u3.save()


