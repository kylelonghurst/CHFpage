from django.conf import settings
from django import forms
from django_mako_plus.controller import view_function
from homepage import models as hmod
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')


############################################################
#### Gets all of the venues and sends to venues.html.

@view_function
def process_request(request):
	params = {}

	venues = hmod.Venue.objects.all()

	params['venues'] = venues

	return templater.render_to_response(request, 'venue.html', params)


############################################################
#### Edits one venue

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def edit(request):
	params = {}

	try:
		venue = hmod.Venue.objects.get(id=request.urlparams[0])
	except hmod.Venue.DoesNotExist:
		return HttpResponseRedirect('/homepage/venue/')

	form = VenueEditForm(initial={
		'name': venue.name,
		'address': venue.address,
		'city': venue.city,
		'state': venue.state,
		'zip': venue.zip,
		'email': venue.email,
		})
	if request.method == 'POST':
		form = VenueEditForm(request.POST)
		form.venueid = venue.id
		if form.is_valid():
			venue.name = form.cleaned_data['name']
			venue.address = form.cleaned_data['address']
			venue.city = form.cleaned_data['city']
			venue.state = form.cleaned_data['state']
			venue.zip = form.cleaned_data['zip']
			venue.email = form.cleaned_data['email']
			venue.save()
			return HttpResponseRedirect('/homepage/venue/')

	params['form'] = form
	params['venue'] = venue
	return templater.render_to_response(request, 'venue.edit.html', params)  

class VenueEditForm(forms.Form):
	name = forms.CharField(required=True, min_length=1, max_length=100)
	address = forms.CharField(required=True, min_length=1, max_length=100)
	city = forms.CharField(required=True, min_length=1, max_length=100)
	state = forms.CharField(required=True, min_length=1, max_length=100)
	zip = forms.CharField(min_length=1, max_length=5)
	email = forms.EmailField(required=True, min_length=1, max_length=100)


	def clean_name(self):
		if len(self.cleaned_data['name']) < 6:
			raise forms.ValidationError('Please enter a name that is at least 6 characters.')
		return self.cleaned_data['name']

############################################################
#### Creates a new Venue

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def create(request):
	venue = hmod.Venue()
	venue.name = ''
	venue.address = ''
	venue.city = ''
	venue.state = ''
	venue.zip = 00000
	venue.email = ''
	venue.save()

	return HttpResponseRedirect('/homepage/venue.edit/{}/'.format(venue.id))

############################################################
#### Deletes a new Venue

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def delete(request):
	try:
		venue = hmod.Venue.objects.get(id=request.urlparams[0])
	except hmod.Venue.DoesNotExist:
		return HttpResponseRedirect('/homepage/venue/')

	venue.delete()

	return HttpResponseRedirect('/homepage/venue/')



