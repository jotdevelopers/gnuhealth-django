from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from health.models import gnuhealth_pathology
from health_configuration.models import gnuhealth_ethnicity
from health_configuration.forms import ethnicityForm
from health_configuration.models import gnuhealth_occupation
from health_configuration.forms import occupationForm

from django.contrib import messages

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
                latest = gnuhealth_ethnicity.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                ethnicities = gnuhealth_ethnicity.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/patients/ethnicities.html'
                              , {'type': type, 'msg': msg, 'ethnicities': ethnicities})
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
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
    editForm = gnuhealth_ethnicity.objects.get(id=id)
    return render(request, 'health_configuration/patients/ethnicities.html', {'form': editForm, 'type': type})


def updateEthnicity(request, id):
    type = "grid"
    eth = gnuhealth_ethnicity.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_ethnicity(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    eth.save()
    msg = "3"
    ethnicities = gnuhealth_ethnicity.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_configuration/patients/ethnicities.html'
                       , {'type': type, 'msg': msg, 'ethnicities': ethnicities})


def deleteEthnicity(request, id):
    ethnicity = gnuhealth_ethnicity.objects.get(id=id)
    ethnicity.delete()
    type = "grid"
    msg = "2"
    ethnicities = gnuhealth_ethnicity.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/patients/ethnicities.html'
                              , {'type': type, 'msg': msg, 'ethnicities': ethnicities})
def citizenship(request):
    return render(request, 'health_configuration/patients/citizenships.html')


def add_citizenship(request):
    return render(request, 'health_configuration/patients/add_citizenship.html')


def occupation(request):
    type = "grid"
    occupations = gnuhealth_occupation.objects.all()
    return render(request, 'health_configuration/patients/occupations.html'
                  , {'occupations': occupations
                  , 'type': type})


def addOccupation(request):
    if request.method == "POST":
        form = occupationForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                form.save()
                occupations = gnuhealth_occupation.objects.all()
                return render(request, 'health_configuration/patients/occupations.html'
                              , {'type': type, 'msg': msg, 'occupations': occupations})
            except:
                pass
        else:
            return HttpResponse("Invalid Form.")
    else:
        form = occupationForm()
        latest = gnuhealth_occupation.objects.latest('id')

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
        return render(request, 'health_configuration/patients/occupations.html', {'type': type, 'form': form})

def editOccupation(request, id):
    type = "edit"
    form = gnuhealth_occupation.objects.get(id=id)
    #return HttpResponse(form.code)
    return render(request, 'health_configuration/patients/occupations.html', {'form': form, 'type': type})


def updateOccupation(request, id):
    occupation = gnuhealth_occupation.objects.get(id=id)
    form = occupationForm(request.POST, instance=occupation)
    if form.is_valid():
        form.save()
        #return redirect("/health-configuration/ethnicities")
    return render(request, 'health_configuration/patients/occupations.html', {'occupation': occupation})

def deleteOccupation(request, id):
    occupation = gnuhealth_occupation.objects.get(id=id)
    occupation.delete()
    type = "grid"
    msg = "2"
    occupations = gnuhealth_occupation.objects.all()
    return render(request, 'health_configuration/patients/occupations.html'
                              , {'type': type, 'msg': msg, 'occupations': occupations})
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