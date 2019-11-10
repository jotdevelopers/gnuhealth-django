from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Obstetrics module functions start
def obstetric_main(request):
	return render(request, "health_obstetrics/obstetric-main.html")

def obstetric_add(request):
	return render(request, "health_obstetrics/obstetric-add.html")

def perinatal_info_monitors(request):
	return render(request, "health_obstetrics/obstetric-perinatal-info-monitors.html")

def perinatal_info(request):
	return render(request, "health_obstetrics/obstetric-perinatal-info.html")

def prenatal_evaluations(request):
	return render(request, "health_obstetrics/obstetric-prenatal-evaluations.html")

def puerperium_monitor(request):
	return render(request, "health_obstetrics/obstetric-puerperium-monitor.html")
# Obstetrics module functions end
    