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
#### Gets all of the areas and sends to areas.html.

@view_function
def process_request(request):
	params = {}

	areas = hmod.Area.objects.all().order_by('name')

	params['areas'] = areas

	return templater.render_to_response(request, 'area.html', params)


############################################################
#### Edits one area

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def edit(request):
	params = {}

	try:
		area = hmod.Area.objects.get(id=request.urlparams[0])
	except hmod.Area.DoesNotExist:
		return HttpResponseRedirect('/homepage/area/')

	form = AreaEditForm(initial={
		'name': area.name,
		'description': area.description,
		'place_number': area.place_number,
		})
	if request.method == 'POST':
		form = AreaEditForm(request.POST)
		form.areaid = area.id
		if form.is_valid():
			area.name = form.cleaned_data['name']
			area.description = form.cleaned_data['description']
			area.place_number = form.cleaned_data['place_number']
			area.save()
			return HttpResponseRedirect('/homepage/area/')

	params['form'] = form
	params['area'] = area
	return templater.render_to_response(request, 'area.edit.html', params)  

class AreaEditForm(forms.Form):
	name = forms.CharField(required=True, min_length=1, max_length=100)
	description = forms.CharField(required=True, min_length=1, max_length=100)
	place_number = forms.IntegerField(required=True)

	def clean_name(self):
		if len(self.cleaned_data['name']) < 6:
			raise forms.ValidationError('Please enter a name that is at least 6 characters.')
		return self.cleaned_data['name']

############################################################
#### Creates a new area

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def create(request):
	area = hmod.Area()
	area.name = ''
	area.description = ''
	area.place_number = 0
	area.save()

	return HttpResponseRedirect('/homepage/area.edit/{}/'.format(area.id))

############################################################
#### Deletes a new area

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def delete(request):
	try:
		area = hmod.Area.objects.get(id=request.urlparams[0])
	except hmod.Area.DoesNotExist:
		return HttpResponseRedirect('/homepage/area/')

	area.delete()

	return HttpResponseRedirect('/homepage/area/')



