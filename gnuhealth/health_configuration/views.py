from django.shortcuts import render
from django.http import HttpResponse
from health.models import gnuhealth_pathology


# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Create Conditions Views
def condition(request):
    conditions = gnuhealth_pathology.objects.all()
    return render(request, 'health_configuration/conditions/conditions.html', {'conditions': conditions})

def pathologyGroups(request):
    return render(request, 'health_configuration/conditions/pathology_groups.html')

def ethnicity(request):
    return render(request, 'health_configuration/patients/ethnicities.html')

def add_ethnicity(request):
    return render(request, 'health_configuration/patients/add_ethnicity.html')

def citizenship(request):
    return render(request, 'health_configuration/patients/citizenships.html')

def add_citizenship(request):
    return render(request, 'health_configuration/patients/add_citizenship.html')

def occupation(request):
    return render(request, 'health_configuration/patients/occupations.html')

def add_occupation(request):
    return render(request, 'health_configuration/patients/add_occupation.html')

def residence(request):
    return render(request, 'health_configuration/patients/residence.html')

def add_residence(request):
    return render(request, 'health_configuration/patients/add_residence.html')

#
#
# def diseaseCategories(request):
#
#
# # Create Genetics Views
# def diseaseGenes(request):
#
#
# def naturalVariants(request):
#
#
# def variantPhenotypes(request):
#
#
# def proteinRelatedDiseases(request):
#
#
# # Create DX Imaging  Views
# def dxImagingTestTypes(request):
#
#
# def dxImagingTests(request):
#
#
# # Create Functioning and Disability  Views
# def bodyFunctions(request):
#
#
# def bodyStructures(request):
#
#
# # Create Procedure  Views
# def procedures(request):
#
#
# # Create Institutions Views
# def buildings(request):
#
#
# # Create DX Imaging  Views
# def variantPhenotypes(request):
#
#
# def variantPhenotypes(request):