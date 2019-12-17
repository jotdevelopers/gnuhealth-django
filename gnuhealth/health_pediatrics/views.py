from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from health_pediatrics.models import *
from health_pediatrics.forms import *
# Create your views here.

# Pediatrics module functions start

def newborn_main(request):
	return render(request, "health_pediatrics/pediatrics-newborn-main.html")

def psc_main(request):
	return render(request, "health_pediatrics/pediatrics-psc-main.html")

def psc_add(request):
	return render(request, "health_pediatrics/pediatrics-psc-add.html")


def newborn_add(request):
    if request.method == "POST":
        form = newBornForm(request.POST)
        if form.is_valid():
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(newborn_main)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = newBornForm()
        form.fields["id"].initial = gnuhealth_newborn.objects.count()+1
        form.fields["healthprof"].initial = gnuhealth_newborn.objects.count()+100
        return render(request, 'health_pediatrics/pediatrics-newborn-add.html', {'form': form, 'selected': 'Pediatrics New Born'})
	
# Pediatrics module functions end