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
#### Gets all of the inventory and sends to inventory.html.

@view_function
def process_request(request):
	params = {}

	inventories = hmod.Inventory.objects.all().order_by('name')

	params['inventories'] = inventories

	return templater.render_to_response(request, 'inventory.html', params)


############################################################
#### Edits one inventory

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def edit(request):
	params = {}

	try:
		inventory = hmod.Inventory.objects.get(id=request.urlparams[0])
	except hmod.Inventory.DoesNotExist:
		return HttpResponseRedirect('/homepage/inventory/')

	form = InventoryEditForm(initial={
		'name': inventory.name,
		'description': inventory.description,
		'value': inventory.value,
		})
	if request.method == 'POST':
		form = InventoryEditForm(request.POST)
		form.inventoryid = inventory.id
		if form.is_valid():
			inventory.name = form.cleaned_data['name']
			inventory.description = form.cleaned_data['description']
			inventory.value = form.cleaned_data['value']
			inventory.save()
			return HttpResponseRedirect('/homepage/inventory/')

	params['form'] = form
	params['inventory'] = inventory
	return templater.render_to_response(request, 'inventory.edit.html', params)  

class InventoryEditForm(forms.Form):
	name = forms.CharField(required=True, min_length=1, max_length=100)
	description = forms.CharField(required=True, min_length=1, max_length=100)
	value = forms.DecimalField(required=True, max_digits=10)

	def clean_name(self):
		if len(self.cleaned_data['name']) < 6:
			raise forms.ValidationError('Please enter a name that is at least 6 characters.')
		return self.cleaned_data['name']

############################################################
#### Creates a new inventory

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def create(request):
	inventory = hmod.Inventory()
	inventory.name = ''
	inventory.description = ''
	inventory.value = 00.00
	inventory.save()

	return HttpResponseRedirect('/homepage/inventory.edit/{}/'.format(inventory.id))

############################################################
#### Deletes a new inventory

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def delete(request):
	try:
		inventory = hmod.Inventory.objects.get(id=request.urlparams[0])
	except hmod.Inventory.DoesNotExist:
		return HttpResponseRedirect('/homepage/inventory/')

	inventory.delete()

	return HttpResponseRedirect('/homepage/inventory/')



