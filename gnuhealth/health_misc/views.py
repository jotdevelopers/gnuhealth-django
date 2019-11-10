from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Misc module functions start
def pediatrics_growth_chart(request):
	return render(request, "health_misc/misc-pediatrics-growth-charts-who.html")
# Misc module functions end