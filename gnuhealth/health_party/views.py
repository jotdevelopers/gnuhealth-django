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
from health_party.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

def addParty(request):
    if request.method == "POST":
        form = partyForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                #latest = party_party.objects.latest('id')
                #form.fields["id"].initial = latest.id + 1
                form.fields["id"].initial =  1
                form.save()
                parties = party_party.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_party/party.html'
                              , {'type': type, 'msg': msg, 'parties': parties})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = partyForm()
        #latest = party_party.objects.latest('id')
        #form.fields["id"].initial = latest.id + 1
        form.fields["id"].initial =  1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_party/party.html', {'type': type, 'form': form})
      
    
def party(request):
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

def searchResidence(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    residence = country_country.objects.filter(name__startswith=search_text.capitalize())
    if len(residence) == 0:
        residence = country_country.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'residence': residence})