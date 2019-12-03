from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_configuration.models import *
from health_party.models import *
from health_demographics.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

def party(request):
    return render(request, 'health_party/party.html')

def addParty(request):
    return render(request, 'health_party/party.html')

def editParty(request):
    return render(request, 'health_party/party.html')

def updateParty(request):
    return render(request, 'health_party/party.html')

def deleteParty(request):
    return render(request, 'health_party/party.html')

def searchEthnicity(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    ethnic_group = gnuhealth_ethnicity.objects.filter(name__startswith=search_text.capitalize())
    if len(ethnic_group) == 0:
        ethnic_group = gnuhealth_ethnicity.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'ethnic_group': ethnic_group})

def searchCitizenship(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    citizenship = country_country.objects.filter(name__startswith=search_text.capitalize())
    if len(citizenship) == 0:
        citizenship = country_country.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'citizenship': citizenship})

def searchOccupation(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    occupation = gnuhealth_occupation.objects.filter(name__startswith=search_text.capitalize())
    if len(occupation) == 0:
        occupation = gnuhealth_occupation.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'occupation': occupation})


def searchDU(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    du = gnuhealth_du.objects.filter(name__startswith=search_text.capitalize())
    if len(du) == 0:
        du = gnuhealth_du.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'du': du})