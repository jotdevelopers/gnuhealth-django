from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Dx-Imaging module functions start
def dx_imaging_requests(request):
	return render(request, "health_dx_imaging/dx-imaging-requests.html")

def dx_imaging_results(request):
	return render(request, "health_dx_imaging/dx-imaging-results.html")

def dx_imaging_test_types(request):
	return render(request, "health_dx_imaging/dx-imaging-test-types.html")
# Dx-Imaging module functions end    