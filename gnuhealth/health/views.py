
from health.models import *  
from health.forms import *
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


# Create your views here.

#Pages of life module

def index(request):
    pols = gnuhealth_pol.objects.all()
    return render(request, 'health/party.html'  , {'pols':pols})
    
def pols(request):
    type = "grid"
    pols = gnuhealth_pol.objects.all()
    return render(request, 'health/pols.html'
                  , {'pols': pols
                      , 'type': type})
    
def patients(request):
    type = "grid"
    patients = gnuhealth_patient.objects.all()
    return render(request, 'health/patients.html'
                  , {'patients': patients
                      , 'type': type})


def addPatient(request):
    if request.method == "POST":
        form = patientForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_patient.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        id = request.POST['id']
        age = request.POST['age']
        author = request.POST['author']
        create_date = request.POST['create_date']
        create_uid = request.POST['create_uid']
        federation_account = request.POST['federation_account']
        gene = 1
        health_condition = request.POST['health_condition']
        health_condition_code = request.POST['health_condition_code']
        health_condition_text = None
        info = None
        institution = request.POST['institution']
        medical_context = None
        natural_variant = 1
        node = request.POST['node']
        page = request.POST['page']
        page_date = request.POST['page_date']
        page_type = request.POST['page_type']
        person = request.POST['person']
        phenotype = 1
        procedure = request.POST['procedure']
        procedure_code = request.POST['procedure_code']
        procedure_text = None
        relevance = request.POST['relevance']
        social_context = None
        summary = request.POST['summary']
        write_date = request.POST['write_date']
        write_uid = request.POST['write_uid']
        fsync = True

        patient = gnuhealth_patient(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,age = age,
        author = author,
        federation_account =federation_account,
        gene = gene,
        health_condition = health_condition,
        health_condition_code = health_condition_code,
        health_condition_text = health_condition_text,
        info = info,
        institution = institution,
        medical_context = medical_context,
        natural_variant = natural_variant,
        node = node,
        page = page,
        page_date = page_date,
        page_type = page_type,
        person = person,
        phenotype = phenotype,
        procedure = procedure,
        procedure_code = procedure_code,
        procedure_text = procedure_text,
        relevance = relevance,
        social_context = social_context,
        summary = summary,
        fsync = fsync)
        patient.save()
        patients = gnuhealth_pol.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health/patients.html'
                              , {'type': type, 'msg': msg, 'patients': patients})
            #except:
             #   pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = patientForm()
        latest = gnuhealth_patient.objects.latest('id')
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
        return render(request, 'health/patients.html', {'type': type, 'form': form})


def editPatient(request, id):
    type = "edit"
    editForm = gnuhealth_patient.objects.get(id=id)
    return render(request, 'health/patients.html', {'form': editForm, 'type': type})


def updatePatient(request, id):
    type = "grid"
    patient = gnuhealth_patient.objects.get(id=id)
    id = patient.id
    age = request.POST['age']
    author = request.POST['author']
    create_date = patient.create_date
    create_uid = patient.create_uid
    federation_account = request.POST['federation_account']
    gene = 1
    health_condition = request.POST['health_condition']
    health_condition_code = request.POST['health_condition_code']
    health_condition_text = None
    info = None
    institution = request.POST['institution']
    medical_context = None
    natural_variant = 1
    node = request.POST['node']
    page = request.POST['page']
    page_date = request.POST['page_date']
    page_type = request.POST['page_type']
    person = request.POST['person']
    phenotype = 1
    procedure = request.POST['procedure']
    procedure_code = request.POST['procedure_code']
    procedure_text = None
    relevance = request.POST['relevance']
    social_context = None
    summary = request.POST['summary']
    write_date = patient.write_date
    write_uid = patient.write_uid
    fsync = True

    patient = gnuhealth_patient(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,age = age,
        author = author,
        federation_account =federation_account,
        gene = gene,
        health_condition = health_condition,
        health_condition_code = health_condition_code,
        health_condition_text = health_condition_text,
        info = info,
        institution = institution,
        medical_context = medical_context,
        natural_variant = natural_variant,
        node = node,
        page = page,
        page_date = page_date,
        page_type = page_type,
        person = person,
        phenotype = phenotype,
        procedure = procedure,
        procedure_code = procedure_code,
        procedure_text = procedure_text,
        relevance = relevance,
        social_context = social_context,
        summary = summary,
        fsync = fsync)
    patient.save()
    
    msg = "3"
    patients = gnuhealth_pol.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health/patients.html'
                  , {'type': type, 'msg': msg, 'patients': patients})


def deletePatient(request, id):
    patient = gnuhealth_patient.objects.get(id=id)
    patient.delete()
    type = "grid"
    msg = "2"
    patients = gnuhealth_patient.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health/patients.html'
                  , {'type': type, 'msg': msg, 'patients': patients})




def addPol(request):
    if request.method == "POST":
        form = polForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_pol.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        id = request.POST['id']
        age = request.POST['age']
        author = request.POST['author']
        create_date = request.POST['create_date']
        create_uid = request.POST['create_uid']
        federation_account = request.POST['federation_account']
        gene = 1
        health_condition = request.POST['health_condition']
        health_condition_code = request.POST['health_condition_code']
        health_condition_text = None
        info = None
        institution = request.POST['institution']
        medical_context = None
        natural_variant = 1
        node = request.POST['node']
        page = request.POST['page']
        page_date = request.POST['page_date']
        page_type = request.POST['page_type']
        person = request.POST['person']
        phenotype = 1
        procedure = request.POST['procedure']
        procedure_code = request.POST['procedure_code']
        procedure_text = None
        relevance = request.POST['relevance']
        social_context = None
        summary = request.POST['summary']
        write_date = request.POST['write_date']
        write_uid = request.POST['write_uid']
        fsync = True

        pol = gnuhealth_pol(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,age = age,
        author = author,
        federation_account =federation_account,
        gene = gene,
        health_condition = health_condition,
        health_condition_code = health_condition_code,
        health_condition_text = health_condition_text,
        info = info,
        institution = institution,
        medical_context = medical_context,
        natural_variant = natural_variant,
        node = node,
        page = page,
        page_date = page_date,
        page_type = page_type,
        person = person,
        phenotype = phenotype,
        procedure = procedure,
        procedure_code = procedure_code,
        procedure_text = procedure_text,
        relevance = relevance,
        social_context = social_context,
        summary = summary,
        fsync = fsync)
        pol.save()
        pols = gnuhealth_pol.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health/pols.html'
                              , {'type': type, 'msg': msg, 'pols': pols})
            #except:
             #   pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = polForm()
        latest = gnuhealth_pol.objects.latest('id')
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
        return render(request, 'health/pols.html', {'type': type, 'form': form})


def editPol(request, id):
    type = "edit"
    editForm = gnuhealth_pol.objects.get(id=id)
    return render(request, 'health/pols.html', {'form': editForm, 'type': type})


def updatePol(request, id):
    type = "grid"
    pol = gnuhealth_pol.objects.get(id=id)
    id = pol.id
    age = request.POST['age']
    author = request.POST['author']
    create_date = pol.create_date
    create_uid = pol.create_uid
    federation_account = request.POST['federation_account']
    gene = 1
    health_condition = request.POST['health_condition']
    health_condition_code = request.POST['health_condition_code']
    health_condition_text = None
    info = None
    institution = request.POST['institution']
    medical_context = None
    natural_variant = 1
    node = request.POST['node']
    page = request.POST['page']
    page_date = request.POST['page_date']
    page_type = request.POST['page_type']
    person = request.POST['person']
    phenotype = 1
    procedure = request.POST['procedure']
    procedure_code = request.POST['procedure_code']
    procedure_text = None
    relevance = request.POST['relevance']
    social_context = None
    summary = request.POST['summary']
    write_date = pol.write_date
    write_uid = pol.write_uid
    fsync = True

    pol = gnuhealth_pol(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,age = age,
        author = author,
        federation_account =federation_account,
        gene = gene,
        health_condition = health_condition,
        health_condition_code = health_condition_code,
        health_condition_text = health_condition_text,
        info = info,
        institution = institution,
        medical_context = medical_context,
        natural_variant = natural_variant,
        node = node,
        page = page,
        page_date = page_date,
        page_type = page_type,
        person = person,
        phenotype = phenotype,
        procedure = procedure,
        procedure_code = procedure_code,
        procedure_text = procedure_text,
        relevance = relevance,
        social_context = social_context,
        summary = summary,
        fsync = fsync)
    pol.save()
    
    msg = "3"
    pols = gnuhealth_pol.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health/pols.html'
                  , {'type': type, 'msg': msg, 'pols': pols})


def deletePol(request, id):
    pol = gnuhealth_pol.objects.get(id=id)
    pol.delete()
    type = "grid"
    msg = "2"
    pols = gnuhealth_pol.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health/pols.html'
                  , {'type': type, 'msg': msg, 'pols': pols})



def searchPerson(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    person = party_party.objects.filter(name__startswith=search_text.capitalize())

    if len(person) == 0:
        person = party_party.objects.filter(id=search_text)

    return render_to_response('health/js/ajax-search.html', {'person': person})

def searchInstitution(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    institution = gnuhealth_institution.objects.filter(name__startswith=search_text.capitalize())

    if len(institution) == 0:
        institution = gnuhealth_institution.objects.filter(id=search_text)

    return render_to_response('health/js/ajax-search.html', {'institution': institution})

def searchCondition(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    condition = gnuhealth_pathology.objects.filter(name__startswith=search_text.capitalize())

    if len(condition) == 0:
        condition = gnuhealth_pathology.objects.filter(id=search_text)

    return render_to_response('health/js/ajax-search.html', {'condition': condition})

def searchProcedure(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    procedure = gnuhealth_procedure.objects.filter(name__startswith=search_text.capitalize())

    if len(procedure) == 0:
        procedure = gnuhealth_procedure.objects.filter(id=search_text)

    return render_to_response('health/js/ajax-search.html', {'procedure': procedure})

