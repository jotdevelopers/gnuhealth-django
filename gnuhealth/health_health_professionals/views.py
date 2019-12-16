from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_health_professionals.models import *
from health_party.models import *
from health_institutions.models import *
from health_party.models import *
from health_health_professionals.forms import *
from health_configuration.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def healthprofs(request):
    type = "grid"
    healthprofs = gnuhealth_healthprofessional.objects.all()
    return render(request, 'health_health_professionals/healthprofs.html'
                  , {'healthprofs': healthprofs
                      , 'type': type})


def addHealthProf(request):
    if request.method == "POST":
        form = healthProfForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_healthprofessional.objects.latest('id')
        form.fields["id"].initial = latest.id+ 1

        active = True
        info = None
        code = request.POST['code']
        name = request.POST['name']
        institution = request.POST['institution']
        id = request.POST['id']
        create_date = request.POST['create_date']
        write_date = request.POST['write_date']
        create_uid = request.POST['create_uid']
        write_uid = request.POST['write_uid']
        main_specialty = None
        prof = gnuhealth_healthprofessional(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, info=info, code=code, institution=institution, active=active,
                              )
        prof.save()
        #form.save()
        healthprofs = gnuhealth_healthprofessional.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_health_professionals/healthprofs.html'
                              , {'type': type, 'msg': msg, 'healthprofs': healthprofs})
            #except:
             #   pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = healthProfForm()
        latest = gnuhealth_healthprofessional.objects.latest('id')
        form.fields["id"].initial = latest.id+ 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_health_professionals/healthprofs.html', {'type': type, 'form': form})


def editHealthProf(request, id):
    type = "edit"
    editForm = gnuhealth_healthprofessional.objects.get(id=id)
    return render(request, 'health_health_professionals/healthprofs.html', {'form': editForm, 'type': type})


def updateHealthProf(request, id):
    type = "grid"
    prof = gnuhealth_healthprofessional.objects.get(id=id)
    
    active = True
    info = None
    code = request.POST['code']
    name = request.POST['name']
    institution = request.POST['institution']
    id = prof.id
    create_date = request.POST['create_date']
    write_date = request.POST['write_date']
    create_uid = request.POST['create_uid']
    write_uid = request.POST['write_uid']
    main_specialty = None
    prof = gnuhealth_healthprofessional(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, info=info, code=code, institution=institution, active=active,
                              )
    prof.save()
    msg = "3"
    healthprofs = gnuhealth_healthprofessional.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_health_professionals/healthprofs.html'
                  , {'type': type, 'msg': msg, 'healthprofs': healthprofs})


def deleteHealthProf(request, id):
    HealthProf = gnuhealth_healthprofessional.objects.get(id=id)
    HealthProf.delete()
    type = "grid"
    msg = "2"
    healthprofs = gnuhealth_healthprofessional.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_health_professionals/healthprofs.html'
                  , {'type': type, 'msg': msg, 'healthprofs': healthprofs})

def searchProf(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    profs = party_party.objects.filter(name__startswith=search_text.capitalize())

    if len(profs) == 0:
        profs = party_party.objects.filter(id=search_text)

    return render_to_response('health_health_professionals/js/ajax-search.html', {'profs': profs})

def searchInstitutionProf(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    institutions = gnuhealth_institution.objects.filter(name__startswith=search_text.capitalize())

    if len(institutions) == 0:
        institutions = gnuhealth_institution.objects.filter(id=search_text)

    return render_to_response('health_health_professionals/js/ajax-search.html', {'institutions': institutions})