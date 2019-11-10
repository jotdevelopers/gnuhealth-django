from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Medicaments module functions start
def medicament_main(request):
	return render(request, "health_medicaments/medicaments-medicament.html")

def medication_frequencies(request):
	return render(request, "health_medicaments/medicaments-medication-frequencies.html")
# Medicaments module functions end