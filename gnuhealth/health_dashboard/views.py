from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "health_dashboard/index.html")

def coming_soon(request):
	return render(request, "health_dashboard/coming-soon.html")