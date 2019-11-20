from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from health.models import gnuhealth_pathology

from health_configuration.models import *
from health_configuration.forms import *

from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Create Conditions Views
def condition(request):
    conditions = gnuhealth_pathology.objects.all()
    return render(request, 'health_configuration/conditions/conditions.html', {'conditions': conditions})

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
        form.fields['write_date'].widget.attrs['readonly'] = True
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
        form.fields['write_date'].widget.attrs['readonly'] = True
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

def genes(request):
    type = "grid"
    genes = gnuhealth_disease_genes.objects.all()
    return render(request, 'health_configuration/genetics/genes.html', {'type': type, 'genes': genes})

def editGenes(request, id):
    type = "edit"
    editForm = gnuhealth_disease_genes.objects.get(id=id)
    return render(request, 'health_configuration/genetics/genes.html', {'form': editForm, 'type': type})

def updateGenes(request, id):
    type = "grid"
    gene = gnuhealth_disease_genes.objects.get(id=id)
    gene.name = request.POST['name']
    gene.long_name = request.POST['long_name']
    gene.protein_name = request.POST['protein_name']
    gene.chromosome = request.POST['chromosome']
    gene.location = request.POST['location']
    gene.gene_id = request.POST['gene_id']

    gene.gene_id = gene.id
    gene.create_date = gene.create_date
    gene.write_date = gene.write_date
    gene.create_uid = gene.create_uid
    gene.write_uid = gene.write_uid

    gene.save()
    genes = gnuhealth_disease_genes.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('genes')


def deleteGenes(request, id):
    gene = gnuhealth_disease_genes.objects.get(id=id)
    gene.delete()
    type = "grid"
    genes = gnuhealth_disease_genes.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('genes')


def addGenes(request):
    if request.method == "POST":
        form = genesForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_disease_genes.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                genes = gnuhealth_disease_genes.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('genes')
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = genesForm()
        latest = gnuhealth_disease_genes.objects.latest('id')
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
        return render(request, 'health_configuration/genetics/genes.html', {'type': type, 'form': form})
    
def varients(request):
    type = "grid"
    varients = gnuhealth_gene_varient.objects.all()
    return render(request, 'health_configuration/genetics/varient.html', {'type': type, 'varients': varients})

def editVarient(request, id):
    type = "edit"
    editForm = gnuhealth_gene_varient.objects.get(id=id)
    return render(request, 'health_configuration/genetics/varient.html', {'form': editForm, 'type': type})

def updateVarient(request, id):
    type = "grid"
    varient = gnuhealth_gene_varient.objects.get(id=id)
    varient.name = request.POST['name']
    varient.aa_change = request.POST['aa_change']
    varient.protein_name = request.POST['varient']
  
    varient.id = id
    varient.create_date = varient.create_date
    varient.write_date = varient.write_date
    varient.create_uid = varient.create_uid
    varient.write_uid = varient.write_uid

    varient.save()
    varients = gnuhealth_gene_varient.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('genes')


def deleteVarient(request, id):
    varient = gnuhealth_gene_varient.objects.get(id=id)
    varient.delete()
    type = "grid"
    varients = gnuhealth_gene_varient.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('varients')


def addVarient(request):
    if request.method == "POST":
        form = varientForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_gene_varient.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                genes = gnuhealth_gene_varient.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('genes')
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = varientForm()
        latest = gnuhealth_gene_varient.objects.latest('id')
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
        return render(request, 'health_configuration/genetics/varients.html', {'type': type, 'form': form})

def pathologyGroups(request):
    type = "grid"
    tempPathologyGroups = gnuhealth_pathology_group.objects.all()
    return render(request, 'health_configuration/conditions/pathology_groups.html', {'type': type, 'tempPathologyGroups': tempPathologyGroups})

def addPathologyGroups(request):
    if request.method == "POST":
        form = pathologyGroupsForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                latest = gnuhealth_pathology_group.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('pathologyGroups')
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = pathologyGroupsForm()
        latest = gnuhealth_pathology_group.objects.latest('id')
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
        return render(request, 'health_configuration/conditions/pathology_groups.html', {'type': type, 'form': form})

def editPathologyGroups(request, id):
    type = "edit"
    editForm = gnuhealth_pathology_group.objects.get(id=id)
    return render(request, 'health_configuration/conditions/pathology_groups.html', {'form': editForm, 'type': type})

def updatePathologyGroups(request, id):
    temp = gnuhealth_pathology_group.objects.get(id=id)
    temp.code = request.POST['code']
    temp.desc = request.POST['desc']
    temp.info = request.POST['info']
    temp.name = request.POST['name']
  
    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('pathologyGroups')

def deletePathologyGroups(request, id):
    temp = gnuhealth_pathology_group.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('pathologyGroups')

def categories(request):
    type = "grid"
    tempCategories = gnuhealth_pathology_category.objects.all()
    return render(request, 'health_configuration/conditions/categories.html', {'type': type, 'tempCategories': tempCategories})

def addCategories(request):
    if request.method == "POST":
        form = categoriesForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_pathology_category.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('categories')
            except:
                pass
        else:         
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = categoriesForm()
        latest = gnuhealth_pathology_category.objects.latest('id')
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
        return render(request, 'health_configuration/conditions/categories.html', {'type': type, 'form': form})

def editCategories(request, id):
    type = "edit"
    editForm = gnuhealth_pathology_category.objects.get(id=id)
    return render(request, 'health_configuration/conditions/categories.html', {'form': editForm, 'type': type})

def updateCategories(request, id):
    temp = gnuhealth_pathology_category.objects.get(id=id)
    temp.name = request.POST['name']
  
    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('categories')

def deleteCategories(request, id):
    temp = gnuhealth_pathology_category.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('categories')

def bodyFunctions(request):
    type = "grid"
    tempBodyFunctions = gnuhealth_body_function.objects.all()
    return render(request, 'health_configuration/functionality_disability/body_functions.html', {'type': type, 'tempBodyFunctions': tempBodyFunctions})

def addBodyFunctions(request):
    if request.method == "POST":
        form = bodyFunctionsForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_body_function.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('bodyFunctions')
            except:
                pass
        else:         
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = bodyFunctionsForm()
        latest = gnuhealth_body_function.objects.latest('id')
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
        return render(request, 'health_configuration/functionality_disability/body_functions.html', {'type': type, 'form': form})

def editBodyFunctions(request, id):
    type = "edit"
    editForm = gnuhealth_body_function.objects.get(id=id)
    return render(request, 'health_configuration/functionality_disability/body_functions.html', {'form': editForm, 'type': type})

def updateBodyFunctions(request, id):
    temp = gnuhealth_body_function.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']
  
    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('bodyFunctions')

def deleteBodyFunctions(request, id):
    temp = gnuhealth_body_function.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('bodyFunctions')

def bodyStructures(request):
    type = "grid"
    tempBodyStructures = gnuhealth_body_structure.objects.all()
    return render(request, 'health_configuration/functionality_disability/body_structures.html', {'type': type, 'tempBodyStructures': tempBodyStructures})

def addBodyStructures(request):
    if request.method == "POST":
        form = bodyStructuresForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_body_structure.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('bodyStructures')
            except:
                pass
        else:         
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = bodyStructuresForm()
        latest = gnuhealth_body_structure.objects.latest('id')
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
        return render(request, 'health_configuration/functionality_disability/body_structures.html', {'type': type, 'form': form})

def editBodyStructures(request, id):
    type = "edit"
    editForm = gnuhealth_body_structure.objects.get(id=id)
    return render(request, 'health_configuration/functionality_disability/body_structures.html', {'form': editForm, 'type': type})

def updateBodyStructures(request, id):
    temp = gnuhealth_body_structure.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']
  
    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('bodyStructures')

def deleteBodyStructures(request, id):
    temp = gnuhealth_body_structure.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('bodyStructures')

def activityParticipation(request):
    type = "grid"
    tempActivityParticipation = gnuhealth_activity_and_participation.objects.all()
    return render(request, 'health_configuration/functionality_disability/activity_patricipation.html', {'type': type, 'tempActivityParticipation': tempActivityParticipation})

def addActivityParticipation(request):
    if request.method == "POST":
        form = activityParticipationForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_activity_and_participation.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('activityParticipation')
            except:
                pass
        else:         
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = activityParticipationForm()
        latest = gnuhealth_activity_and_participation.objects.latest('id')
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
        return render(request, 'health_configuration/functionality_disability/activity_patricipation.html', {'type': type, 'form': form})

def editActivityParticipation(request, id):
    type = "edit"
    editForm = gnuhealth_activity_and_participation.objects.get(id=id)
    return render(request, 'health_configuration/functionality_disability/activity_patricipation.html', {'form': editForm, 'type': type})

def updateActivityParticipation(request, id):
    temp = gnuhealth_activity_and_participation.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']
  
    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('activityParticipation')

def deleteActivityParticipation(request, id):
    temp = gnuhealth_activity_and_participation.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('activityParticipation')

def environmentalFactor(request):
    type = "grid"
    tempEnvironmentalFactor = gnuhealth_environmental_factor.objects.all()
    return render(request, 'health_configuration/functionality_disability/environmental_factor.html', {'type': type, 'tempEnvironmentalFactor': tempEnvironmentalFactor})

def addEnvironmentalFactor(request):
    if request.method == "POST":
        form = environmentalFactorForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_environmental_factor.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('environmentalFactor')
            except:
                pass
        else:         
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = environmentalFactorForm()
        latest = gnuhealth_environmental_factor.objects.latest('id')
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
        return render(request, 'health_configuration/functionality_disability/environmental_factor.html', {'type': type, 'form': form})

def editEnvironmentalFactor(request, id):
    type = "edit"
    editForm = gnuhealth_environmental_factor.objects.get(id=id)
    return render(request, 'health_configuration/functionality_disability/environmental_factor.html', {'form': editForm, 'type': type})

def updateEnvironmentalFactor(request, id):
    temp = gnuhealth_environmental_factor.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']
  
    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('environmentalFactor')

def deleteEnvironmentalFactor(request, id):
    temp = gnuhealth_environmental_factor.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('environmentalFactor')

def dietBelief(request):
    type = "grid"
    tempDietBelief = gnuhealth_diet_belief.objects.all()
    return render(request, 'health_configuration/misc/diet_belief.html', {'type': type, 'tempDietBelief': tempDietBelief})

def addDietBelief(request):
    if request.method == "POST":
        form = dietBeliefForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_diet_belief.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('dietBelief')
            except:
                pass
        else:         
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = dietBeliefForm()
        latest = gnuhealth_diet_belief.objects.latest('id')
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
        return render(request, 'health_configuration/misc/diet_belief.html', {'type': type, 'form': form})

def editDietBelief(request, id):
    type = "edit"
    editForm = gnuhealth_diet_belief.objects.get(id=id)
    return render(request, 'health_configuration/misc/diet_belief.html', {'form': editForm, 'type': type})

def updateDietBelief(request, id):
    temp = gnuhealth_diet_belief.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']
    temp.description = request.POST['description']
  
    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('dietBelief')

def deleteDietBelief(request, id):
    temp = gnuhealth_diet_belief.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('dietBelief')

def dietTherapeutic(request):
    type = "grid"
    tempDietTherapeutic = gnuhealth_diet_therapeutic.objects.all()
    return render(request, 'health_configuration/misc/diet_therapeutic.html', {'type': type, 'tempDietTherapeutic': tempDietTherapeutic})

def addDietTherapeutic(request):
    if request.method == "POST":
        form = dietTherapeuticForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_diet_therapeutic.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')                
                return redirect('dietTherapeutic')
            except:
                pass
        else:         
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = dietTherapeuticForm()
        latest = gnuhealth_diet_therapeutic.objects.latest('id')
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
        return render(request, 'health_configuration/misc/diet_therapeutic.html', {'type': type, 'form': form})

def editDietTherapeutic(request, id):
    type = "edit"
    editForm = gnuhealth_diet_therapeutic.objects.get(id=id)
    return render(request, 'health_configuration/misc/diet_therapeutic.html', {'form': editForm, 'type': type})

def updateDietTherapeutic(request, id):
    temp = gnuhealth_diet_therapeutic.objects.get(id=id)
    temp.name = request.POST['name']
    temp.code = request.POST['code']
    temp.description = request.POST['description']
  
    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('dietTherapeutic')

def deleteDietTherapeutic(request, id):
    temp = gnuhealth_diet_therapeutic.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('dietTherapeutic')

def pediatricsGrowthChart(request):
    type = "grid"
    tempPediatricsGrowthChart = gnuhealth_pediatrics_growth_charts_who.objects.all()
    return render(request, 'health_configuration/misc/pediatrics_growth_chart.html', {'type': type, 'tempPediatricsGrowthChart': tempPediatricsGrowthChart})

def addPediatricsGrowthChart(request):
    if request.method == "POST":
        form = pediatricGrowthChartForm(request.POST)
        if form.is_valid():
            try:
                latest = gnuhealth_pediatrics_growth_charts_who.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')             
                return redirect('pediatricsGrowthChart')
            except:
                pass
        else:         
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = pediatricGrowthChartForm()
        latest = gnuhealth_pediatrics_growth_charts_who.objects.latest('id')
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
        return render(request, 'health_configuration/misc/pediatrics_growth_chart.html', {'type': type, 'form': form})

def editPediatricsGrowthChart(request, id):
    type = "edit"
    editForm = gnuhealth_pediatrics_growth_charts_who.objects.get(id=id)
    return render(request, 'health_configuration/misc/pediatrics_growth_chart.html', {'form': editForm, 'type': type})

def updatePediatricsGrowthChart(request, id):
    temp = gnuhealth_pediatrics_growth_charts_who.objects.get(id=id)
    temp.indicator = request.POST['indicator']
    temp.measure = request.POST['measure']
    temp.sex = request.POST['sex']
    temp.month = request.POST['month']
    temp.type = request.POST['type']
    temp.value = request.POST['value']
  
    temp.id = id
    temp.create_date = temp.create_date
    temp.write_date = temp.write_date
    temp.create_uid = temp.create_uid
    temp.write_uid = temp.write_uid

    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect('pediatricsGrowthChart')

def deletePediatricsGrowthChart(request, id):
    temp = gnuhealth_pediatrics_growth_charts_who.objects.get(id=id)
    temp.delete()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect('pediatricsGrowthChart')

def operationalSectors(request):
    type = "grid"
    opsectors = gnuhealth_operational_sector.objects.all()
    return render(request, 'health_configuration/hospitalization/operational_sectors.html'
                  , {'opsectors': opsectors
                  , 'type': type})

def addOperationalSector(request):
    if request.method == "POST":
        form = operationalSectorForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_operational_sector.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                opsectors = gnuhealth_operational_sector.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/hospitalization/operational_sectors.html'
                              , {'type': type, 'msg': msg, 'opsectors': opsectors})
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = operationalSectorForm()
        latest = gnuhealth_operational_sector.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/hospitalization/operational_sectors.html', {'type': type, 'form': form})


def editOperationalSector(request, id):
    type = "edit"
    editForm = gnuhealth_operational_sector.objects.get(id=id)
    return render(request, 'health_configuration/hospitalization/operational_sectors.html', {'form': editForm, 'type': type})


def updateOperationalSector(request, id):
    type = "grid"
    op = gnuhealth_operational_sector.objects.get(id=id)
    name = request.POST['name']
    info = request.POST['info']
    operational_area = request.POST['operational_area']
    op_id = op.id
    create_date = op.create_date
    write_date = op.write_date
    create_uid = op.create_uid
    write_uid = op.write_uid
    op = gnuhealth_operational_sector(id=op_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, info=info, operational_area=operational_area)
    op.save()
    msg = "3"
    opsectors = gnuhealth_operational_sector.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_configuration/hospitalization/operational_sectors.html'
                       , {'type': type, 'msg': msg, 'opsectors': opsectors})


def deleteOperationalSector(request, id):
    opsector = gnuhealth_operational_sector.objects.get(id=id)
    opsector.delete()
    type = "grid"
    msg = "2"
    opsectors = gnuhealth_operational_sector.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/hospitalization/operational_sectors.html'
                              , {'type': type, 'msg': msg, 'opsectors': opsectors})

def operationalAreas(request):
    type = "grid"
    opareas = gnuhealth_operational_area.objects.all()
    return render(request, 'health_configuration/hospitalization/operational_areas.html'
                  , {'opareas': opareas
                  , 'type': type})

def addOperationalArea(request):
    if request.method == "POST":
        form = operationalAreaForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_operational_area.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                opareas = gnuhealth_operational_area.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/hospitalization/operational_areas.html'
                              , {'type': type, 'msg': msg, 'opareas': opareas})
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = operationalAreaForm()
        latest = gnuhealth_operational_area.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_configuration/hospitalization/operational_areas.html', {'type': type, 'form': form})


def editOperationalArea(request, id):
    type = "edit"
    editForm = gnuhealth_operational_area.objects.get(id=id)
    return render(request, 'health_configuration/hospitalization/operational_areas.html', {'form': editForm, 'type': type})


def updateOperationalArea(request, id):
    type = "grid"
    op = gnuhealth_operational_area.objects.get(id=id)
    name = request.POST['name']
    info = request.POST['info']
    op_id = op.id
    create_date = op.create_date
    write_date = op.write_date
    create_uid = op.create_uid
    write_uid = op.write_uid
    op = gnuhealth_operational_area(id=op_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, info=info)
    op.save()
    msg = "3"
    opareas = gnuhealth_operational_area.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_configuration/hospitalization/operational_areas.html'
                       , {'type': type, 'msg': msg, 'opareas': opareas})


def deleteOperationalArea(request, id):
    oparea = gnuhealth_operational_area.objects.get(id=id)
    oparea.delete()
    type = "grid"
    msg = "2"
    opareas = gnuhealth_operational_area.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/hospitalization/operational_areas.html'
                              , {'type': type, 'msg': msg, 'opareas': opareas})
