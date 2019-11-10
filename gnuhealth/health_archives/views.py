from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

# Archives module functions start
def archives_main(request):
	return render(request, "health_archives/medical-archives-main.html")

def archives_add(request):
	return render(request, "health_archives/medical-archives-add.html")
# Archives module functions end    