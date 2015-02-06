from django.conf import settings
from django_mako_plus.controller import view_function
from homepage import models as hmod
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller.router import get_renderer
from random import randint

templater = get_renderer('homepage')

from datetime import datetime

@view_function
def process_request(request):
  params = {}

  #users = hmod.SiteUser.objects.
  randnum = randint(1,100)
  params['randnum'] = randnum

  return templater.render_to_response(request, 'index.html', params)