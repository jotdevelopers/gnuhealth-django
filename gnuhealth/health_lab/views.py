from django.shortcuts import render
from django.http import HttpResponse
from health_lab.models import gnuhealth_patient_lab_test
# Create your views here.

def index(request):
    labs = gnuhealth_patient_lab_test.objects.all()
    return render(request, 'health_lab/index.html')

def addlabtestrequest(request):
    return render(request,'health_lab/add-lab-test-request.html') #,{'form':form})  

def labtestresult(request):
    return render(request, 'health_lab/lab-test-results.html')

    

# Laboratory module functions start
def lab_test_types(request):
	return render(request, "health_laboratory/laboratory-lab-test-types.html")

def lab_test_units(request):
	return render(request, "health_laboratory/laboratory-lab-test-units.html")
# Laboratory module functions end
