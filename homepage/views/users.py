from django.conf import settings
from django import forms
from django_mako_plus.controller import view_function
from homepage import models as hmod
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')


############################################################
#### Gets all of the users and sends to users.html.

@view_function
def process_request(request):
  params = {}

  users = hmod.User.objects.all()

  params['users'] = users

  return templater.render_to_response(request, 'users.html', params)


############################################################
#### Edits one user

@view_function
def edit(request):
  params = {}

  try:
  	user = hmod.User.objects.get(id=request.urlparams[0])
  except hmod.User.DoesNotExist:
  	return HttpResponseRedirect('/homepage/users/')

  form = UserEditForm(initial={
  	'username': user.username,
  	'first_name': user.first_name,
  	'last_name': user.last_name,
  	'email': user.email,
  	'password': user.password,
  	})
  if request.method == 'POST':
  	form = UserEditForm(request.POST)
  	form.userid = user.id
  	if form.is_valid():
  		user.username = form.cleaned_data['username']
  		user.first_name = form.cleaned_data['first_name']
  		user.last_name = form.cleaned_data['last_name']
  		user.email = form.cleaned_data['email']
  		user.set_password(form.cleaned_data['password'])
  		user.save()
  		return HttpResponseRedirect('/homepage/users/')

  params['form'] = form
  params['user'] = user
  return templater.render_to_response(request, 'users.edit.html', params)  

class UserEditForm(forms.Form):
	username = forms.CharField(required=True, min_length=1, max_length=100)
	first_name = forms.CharField(required=True, min_length=1, max_length=100)
	last_name = forms.CharField(required=True, min_length=1, max_length=100)
	email = forms.EmailField(required=True, min_length=1, max_length=100)
	password = forms.CharField(required=True, min_length=1, max_length=100)

	def clean_username(self):
		if len(self.cleaned_data['username']) < 6:
			raise forms.ValidationError('Please enter a username that is at least 6 characters.')
		users_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
		if users_count >= 1:
			raise forms.ValidationError("This username is already taken.")
		return self.cleaned_data['username']

############################################################
#### Creates a new user

@view_function
def create(request):
	user = hmod.User()
	user.username = ''
	user.email = ''
	user.first_name = ''
	user.last_name = ''
	user.first_name = ''
	user.save()

	return HttpResponseRedirect('/homepage/users.edit/{}/'.format(user.id))

############################################################
#### Deletes a new user

@view_function
def delete(request):
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/users/')

	user.delete()

	return HttpResponseRedirect('/homepage/users/')



