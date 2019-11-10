from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Procedures module functions start
def procedures_main(request):
	return render(request, "health_procedures/procedures-main.html")
# Procedures module functions end