from django.shortcuts import render
from django.http import HttpResponse
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