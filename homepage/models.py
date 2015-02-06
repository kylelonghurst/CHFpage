from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


'''This needs to go towards the top'''
class User(AbstractUser):
	#inherited from AbstractBaseUser
    #password
    #last_login

	#inherited from AbstractUser
	#username
    #first_name
    #last_name
    #email
    #is_staff
    #is_active
    #date_joined

    #def get_full_name(self):
    #def get_short_name(self):
    #def email_user(self, subject, message, from_email=None, **kwargs):
    #def get_username(self):
    #def __str__(self):
    #def natural_key(self):
    #def is_anonymous(self):
    #def is_authenticated(self):
    #def set_password(self, raw_password):
    #def check_password(self, raw_password):
    #def setter(raw_password):
    #def set_unusable_password(self):
    #def has_usable_password(self):
    #def get_full_name(self):
    #def get_short_name(self):
    #def get_session_auth_hash(self):

	address1 = models.TextField(max_length=50)
	address2 = models.TextField(max_length=50)
	city = models.TextField(max_length=20)
	state = models.CharField(max_length=2)
	zip = models.IntegerField(max_length=5)
    