from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "health_dashboard/index.html")

def coming_soon(request):
	return render(request, "health_dashboard/coming-soon.html")

#Dashboard

def visitHistory(request):
    return render(request, 'health_dashboard/visitHistory.html'  )

def patientVisits(request):
    return render(request, 'health_dashboard/patientVisits.html'  )

def patientHistory(request):
    return render(request, 'health_dashboard/patientHistory.html'  )

def patientTests(request):
    return render(request, 'health_dashboard/patientTests.html'  )
