from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_configuration.models import *
from health_party.models import *
from health_party.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

def addParty(request):
    if request.method == "POST":
        form = partyForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = party_party.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
                
        #form.fields["id"].initial =  2
        id = request.POST['id']
        active = True
        code = ''
        create_date = request.POST['create_date']
        create_uid = request.POST['create_uid']
        write_date = request.POST['write_date']
        write_uid = request.POST['write_uid']
        name = ''
        replaced_by = 1
        activation_date = request.POST['activation_date']
        alternative_identification = True
        birth_certificate = None
        citizenship = request.POST['citizenship']
        death_certificate = None
        deceased = True
        dob = request.POST['dob']
        du = request.POST['du']
        ethnic_group = request.POST['ethnic_group']
        fed_country = request.POST['citizenship']
        federation_account = request.POST['federation_account']
        gender = request.POST['gender']
        insurance_company_type = request.POST['insurance_company_type']
        internal_user = 1
        is_healthprof = False
        is_institution = False
        is_insurance_company= False
        is_patient = True
        is_person = True
        is_pharmacy = False
        lastname = ''
        marital_status = request.POST['marital_status']
        name_representation = ''
        photo = ''
        ref = ''
        residence = request.POST['residence']
        unidentified = True
        education = request.POST['education']
        occupation = request.POST['occupation']
        fsync = False
        warehouse = 1

        party = party_party(id=id,
                active = active,
                code = code,
                create_date = create_date,
                create_uid = create_uid,
                write_date = write_date,
                write_uid = write_uid,
                name = name,
                replaced_by = replaced_by,
                activation_date = activation_date,
                alternative_identification = alternative_identification,
                birth_certificate = birth_certificate,
                citizenship = citizenship,
                death_certificate = death_certificate,
                deceased = deceased,
                dob = dob,
                du = du,
                ethnic_group = ethnic_group,
                fed_country = fed_country,
                federation_account = federation_account,
                gender = gender,
                insurance_company_type = insurance_company_type,
                internal_user = internal_user,
                is_healthprof = is_healthprof,
                is_institution = is_institution,
                is_insurance_company= is_insurance_company,
                is_patient = is_patient,
                is_person = is_person,
                is_pharmacy = is_pharmacy,
                lastname = lastname,
                marital_status = marital_status,
                name_representation = name_representation,
                photo = photo,
                ref = ref,
                residence = residence,
                unidentified = unidentified,
                education = education,
                occupation = occupation,
                fsync = fsync,
                warehouse = warehouse)
        party.save()
        parties = party_party.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_party/party.html'
                              , {'type': type, 'msg': msg, 'parties': parties})
         #   except:
          #      pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = partyForm()
        latest = party_party.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        #form.fields["id"].initial =  2
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
        return render(request, 'health_party/party.html', {'type': type, 'form': form})
      
    
def party(request):
        return render(request, 'health_party/party.html')


def editParty(request):
    return render(request, 'health_party/party.html')

def updateParty(request):
    return render(request, 'health_party/party.html')

def deleteParty(request):
    return render(request, 'health_party/party.html')

def searchEthnicity(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    ethnic_group = gnuhealth_ethnicity.objects.filter(name__startswith=search_text.capitalize())
    if len(ethnic_group) == 0:
        ethnic_group = gnuhealth_ethnicity.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'ethnic_group': ethnic_group})

def searchCitizenship(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    citizenship = country_country.objects.filter(name__startswith=search_text.capitalize())
    if len(citizenship) == 0:
        citizenship = country_country.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'citizenship': citizenship})

def searchOccupation(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    occupation = gnuhealth_occupation.objects.filter(name__startswith=search_text.capitalize())
    if len(occupation) == 0:
        occupation = gnuhealth_occupation.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'occupation': occupation})


def searchDU(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    du = gnuhealth_du.objects.filter(name__startswith=search_text.capitalize())
    if len(du) == 0:
        du = gnuhealth_du.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'du': du})

def searchResidence(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''
    residence = country_country.objects.filter(name__startswith=search_text.capitalize())
    if len(residence) == 0:
        residence = country_country.objects.filter(id=search_text)

    return render_to_response('health_party/js/ajax-search.html', {'residence': residence})