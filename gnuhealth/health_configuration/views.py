from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from health.models import gnuhealth_pathology
from health_configuration.models import gnuhealth_ethnicity
from health_configuration.forms import ethnicityForm

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
    type = "grid"
    ethnicities = gnuhealth_ethnicity.objects.all()
    return render(request, 'health_configuration/patients/ethnicities.html'
                  , {'ethnicities': ethnicities
                  , 'type': type})

def addEthnicity(request):
    if request.method == "POST":
        form = ethnicityForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                form.save()
                ethnicities = gnuhealth_ethnicity.objects.all()
                return render(request, 'health_configuration/patients/ethnicities.html'
                              , {'type': type, 'msg': msg, 'ethnicities': ethnicities})
            except:
                pass
        else:
            return HttpResponse("Invalid Form.")
    else:
        form = ethnicityForm()
        latest = gnuhealth_ethnicity.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = False
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/patients/ethnicities.html', {'type': type, 'form': form})


def editEthnicity(request, id):
    type = "edit"
    form = gnuhealth_ethnicity.objects.get(id=id)
    return render(request, 'health_configuration/patients/ethnicities.html', {'form': form, 'type': type})


def updateEthnicity(request, id):
    eth = gnuhealth_ethnicity.objects.get(id=id)
    form = ethnicityForm(request.POST, instance=eth)
    if form.is_valid():
        form.save()
        return redirect("/health-configuration/ethnicities")
    return render(request, 'health_configuration/patients/ethnicities.html', {'ethnicity': ethnicity})


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