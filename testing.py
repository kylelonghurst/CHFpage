import os
os.environ["DJANGO_SETTINGS_MODULE"] = "test_dmp.settings"
import django
django.setup()
from django.db import connection
import subprocess
from django.contrib.auth.models import Group, Permission, ContentType

cursor = connection.cursor()

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

# group1 = Group()
# group1.name = 'Admin'
# group1.save()
# group1.permissions.add(permission1)
# permission = Permission.objects.get(id=97)
# group1.permissions.add(permission)

# group2 = Group()
# group2.name = 'Manager'
# group2.save()
# group2.permissions.add(permission2)
# permission = Permission.objects.get(id=98)
# group1.permissions.add(permission)

# group3 = Group()
# group3.name = 'Guest'
# group3.save()
# group3.permissions.add(permission3)
# permission = Permission.objects.get(id=99)
# group1.permissions.add(permission)

# user = hmod.SiteUser.objects.get(id=1)
# user.groups.add(group1)

# user = hmod.SiteUser.objects.get(id=2)
# user.groups.add(group2)

# user = hmod.SiteUser.objects.get(id=3)
# user.groups.add(group3)
