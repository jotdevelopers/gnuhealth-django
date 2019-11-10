from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Ambulance Support module functions start
def ambulances_in_support_req_main(request):
	return render(request, "health_ambulances_support/ambulances-in-support-requests-main.html")

def ambulances_in_support_req_add(request):
	return render(request, "health_ambulances_support/ambulances-in-support-requests-add.html")
# Ambulance Support module functions end    