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
