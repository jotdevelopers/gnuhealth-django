from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

# Federation module functions start
def queue_manager_main(request):
	return render(request, "health_federation/federation-queue-manager-main.html")
# Federation module functions end