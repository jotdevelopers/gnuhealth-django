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