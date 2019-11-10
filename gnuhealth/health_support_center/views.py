from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Support Center module functions start
def support_center_main(request):
	return render(request, "health_support_center/support-center-main.html")

def support_center_add(request):
	return render(request, "health_support_center/support-center-add.html")

def ambulances(request):
	return render(request, "health_support_center/support-center-ambulances.html")
# Support Center module functions end    