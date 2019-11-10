from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

# Nursing module functions start
def ambulatory_care_main(request):
	return render(request, "health_nursing/nursing-ambulatory-care-main.html")

def ambulatory_care_add(request):
	return render(request, "health_nursing/nursing-ambulatory-care-add.html")

def roundings_main(request):
	return render(request, "health_nursing/nursing-roundings-main.html")

def roundings_add(request):
	return render(request, "health_nursing/nursing-roundings-add.html")
# Nursing module functions end    