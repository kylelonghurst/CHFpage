from django.conf import settings
from django import forms
from django_mako_plus.controller import view_function
from homepage import models as hmod
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')

############################################################
#### Logs the user in given their credetials

@view_function
def process_request(request):
  params = {}

  form = LoginForm(initial={
  	})
  if request.method == 'POST':
  	form = LoginForm(request.POST)
  	if form.is_valid():
  		user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
  		login(request, user)
  		return HttpResponseRedirect('/homepage/index/')

  params['form'] = form
  return templater.render_to_response(request, 'login.html', params)  

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(label="Password", widget=forms.PasswordInput)

	def clean(self):
		user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		if user == None:
			raise forms.ValidationError('Sorry you can not come in.')
		return self.cleaned_data