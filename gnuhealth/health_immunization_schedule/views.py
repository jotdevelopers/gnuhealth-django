from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Immunization module functions start
def vaccine_doses(request):
	return render(request, "health_immunization/immunization-vaccine-doses.html")
# Immunization module functions end