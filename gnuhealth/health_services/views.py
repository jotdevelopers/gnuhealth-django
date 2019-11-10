from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

# Health Services module functions start
def health_services_main(request):
	return render(request, "health_services/health-services-main.html")

def health_services_add(request):
	return render(request, "health_services/health-services-add.html")

def created_invoices_main(request):
	return render(request, "health_services/health-services-created-invoices.html")

def created_invoices_add(request):
	return render(request, "health_services/health-services-created-invoices-add.html")
# Health Services module functions end    