from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Pediatrics module functions start

def newborn_main(request):
	return render(request, "health_pediatrics/pediatrics-newborn-main.html")

def newborn_add(request):
	return render(request, "health_pediatrics/pediatrics-newborn-add.html")

def psc_main(request):
	return render(request, "health_pediatrics/pediatrics-psc-main.html")

def psc_add(request):
	return render(request, "health_pediatrics/pediatrics-psc-add.html")
	
# Pediatrics module functions end