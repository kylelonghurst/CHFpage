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
#### Gets all of the SaleItems and sends to SaleItems.html.

@view_function
def process_request(request):
	params = {}

	saleitems = hmod.SaleItem.objects.all().order_by('name')

	params['saleitems'] = saleitems

	return templater.render_to_response(request, 'saleitem.html', params)


############################################################
#### Edits one SaleItem

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def edit(request):
	params = {}

	try:
		saleitem = hmod.SaleItem.objects.get(id=request.urlparams[0])
	except hmod.saleitem.DoesNotExist:
		return HttpResponseRedirect('/homepage/saleitem/')

	form = SaleItemEditForm(initial={
		'name': saleitem.name,
		'description': saleitem.description,
		'low_price': saleitem.low_price,
		'high_price': saleitem.high_price,
		})
	if request.method == 'POST':
		form = SaleItemEditForm(request.POST)
		form.saleitemid = saleitem.id
		if form.is_valid():
			saleitem.name = form.cleaned_data['name']
			saleitem.description = form.cleaned_data['description']
			saleitem.low_price = form.cleaned_data['low_price']
			saleitem.high_price = form.cleaned_data['high_price']
			saleitem.save()
			return HttpResponseRedirect('/homepage/saleitem/')

	params['form'] = form
	params['saleitem'] = saleitem
	return templater.render_to_response(request, 'saleitem.edit.html', params)  

class SaleItemEditForm(forms.Form):
	name = forms.CharField(required=True, min_length=1, max_length=100)
	description = forms.CharField(required=True, min_length=1, max_length=100)
	low_price = forms.DecimalField(required=True, max_digits=10)
	high_price = forms.DecimalField(required=True, max_digits=10)

	def clean_name(self):
		if len(self.cleaned_data['name']) < 6:
			raise forms.ValidationError('Please enter a name that is at least 6 characters.')
		return self.cleaned_data['name']

############################################################
#### Creates a new saleitem

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def create(request):
	saleitem = hmod.SaleItem()
	saleitem.name = ''
	saleitem.description = ''
	saleitem.low_price = 0.00
	saleitem.high_price = 0.00
	saleitem.save()

	return HttpResponseRedirect('/homepage/saleitem.edit/{}/'.format(saleitem.id))

############################################################
#### Deletes a new SaleItem

@view_function
@permission_required('homepage.Manager', login_url='/homepage/permission/')
def delete(request):
	try:
		saleitem = hmod.SaleItem.objects.get(id=request.urlparams[0])
	except hmod.SaleItem.DoesNotExist:
		return HttpResponseRedirect('/homepage/saleitem/')

	saleitem.delete()

	return HttpResponseRedirect('/homepage/saleitem/')



