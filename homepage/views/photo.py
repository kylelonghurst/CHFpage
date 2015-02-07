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
#### Gets all of the photographs and sends to photographs.html.

@view_function
def process_request(request):
	params = {}

	photographs = hmod.Photograph.objects.all()

	params['photographs'] = photographs

	return templater.render_to_response(request, 'photo.html', params)


############################################################
#### Edits one photograph

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def edit(request):
	params = {}

	try:
		photograph = hmod.Photograph.objects.get(id=request.urlparams[0])
	except hmod.Photograph.DoesNotExist:
		return HttpResponseRedirect('/homepage/photo/')

	form = PhotographEditForm(initial={
		'image': photograph.image,
		'date': photograph.date,
		'place': photograph.place,
		})
	if request.method == 'POST':
		form = PhotographEditForm(request.POST)
		form.photographid = photograph.id
		if form.is_valid():
			photograph.image = form.cleaned_data['image']
			photograph.date = form.cleaned_data['date']
			photograph.place = form.cleaned_data['place']
			photograph.save()
			return HttpResponseRedirect('/homepage/photo/')

	params['form'] = form
	params['photograph'] = photograph
	return templater.render_to_response(request, 'photo.edit.html', params)  

class PhotographEditForm(forms.Form):
	image = forms.CharField(required=True, min_length=1, max_length=100)
	date = forms.DateField()
	place = forms.CharField(required=True, min_length=1, max_length=100)

	def clean_image(self):
		if len(self.cleaned_data['image']) < 6:
			raise forms.ValidationError('Please enter a image address that is at least 6 characters.')
		return self.cleaned_data['image']

############################################################
#### Creates a new photograph

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def create(request):
	photograph = hmod.Photograph()
	photograph.name = ''
	photograph.address = ''
	photograph.city = ''
	photograph.state = ''
	photograph.zip = 00000
	photograph.email = ''
	photograph.save()

	return HttpResponseRedirect('/homepage/photo.edit/{}/'.format(photograph.id))

############################################################
#### Deletes a new photograph

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def delete(request):
	try:
		photograph = hmod.Photograph.objects.get(id=request.urlparams[0])
	except hmod.Photograph.DoesNotExist:
		return HttpResponseRedirect('/homepage/photo/')

	photograph.delete()

	return HttpResponseRedirect('/homepage/photo/')



