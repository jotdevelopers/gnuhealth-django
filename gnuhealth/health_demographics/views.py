from datetime import datetime
from django.http import HttpResponse
from health_demographics.models import *
from health_demographics.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health_configuration.models import *
from health_configuration.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from health_party.models import *
from health_operational_area.models import *

# Create your views here.
def index(request): 
    return HttpResponse("Hello, world.")

def families(request):
    type = "grid"
    families = gnuhealth_family.objects.all()
    return render(request, 'health_demographics/families.html'
                  , {'families': families
                  , 'type': type})

def addFamily(request):
    if request.method == "POST":
        form = familyForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_family.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                families = gnuhealth_family.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_demographics/families.html'
                              , {'type': type, 'msg': msg, 'families': families})
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = familyForm()
        latest = gnuhealth_family.objects.latest('id')
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
        return render(request, 'health_demographics/families.html', {'type': type, 'form': form})


def editFamily(request, id):
    type = "edit"
    editForm = gnuhealth_family.objects.get(id=id)
    return render(request, 'health_demographics/families.html', {'form': editForm, 'type': type})


def updateFamily(request, id):
    type = "grid"
    eth = gnuhealth_family.objects.get(id=id)
    name = request.POST['name']
    info = request.POST['info']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_family(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, info=info)
    eth.save()
    msg = "3"
    families = gnuhealth_family.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_demographics/families.html'
                       , {'type': type, 'msg': msg, 'families': families})


def deleteFamily(request, id):
    family = gnuhealth_family.objects.get(id=id)
    family.delete()
    type = "grid"
    msg = "2"
    families = gnuhealth_family.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_demographics/families.html'
                              , {'type': type, 'msg': msg, 'families': families})


def familyMembers(request):
    type = "grid"
    members = gnuhealth_family_member.objects.all()
    return render(request, 'health_demographics/familymembers.html'
                  , {'members': members
                  , 'type': type})

def addFamilyMember(request):
    if request.method == "POST":
        form = familyMemberForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                #latest = gnuhealth_family_member.objects.latest('id')
                #form.fields["id"].initial = latest.id + 1
                form.fields["id"].initial = 1
                form.save()
                members = gnuhealth_family_member.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_demographics/familymembers.html'
                              , {'type': type, 'msg': msg, 'members': members})
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = familyMemberForm()
        #latest = gnuhealth_family_member.objects.latest('id')
        #form.fields["id"].initial = latest.id + 1
        form.fields["id"].initial =  1
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
        return render(request, 'health_demographics/familymembers.html', {'type': type, 'form': form})


def editFamilyMember(request, id):
    type = "edit"
    editForm = gnuhealth_family_member.objects.get(id=id)
    return render(request, 'health_demographics/familymembers.html', {'form': editForm, 'type': type})


def updateFamilyMember(request, id):
    type = "grid"
    eth = gnuhealth_family_member.objects.get(id=id)
    name = request.POST['name']
    role = request.POST['role']
    party = request.POST['party']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_family_member(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, role=role, party=party)
    eth.save()
    msg = "3"
    members = gnuhealth_family_member.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_demographics/familymembers.html'
                       , {'type': type, 'msg': msg, 'members': members})


def deleteFamilyMember(request, id):
    member = gnuhealth_family_member.objects.get(id=id)
    member.delete()
    type = "grid"
    msg = "2"
    members = gnuhealth_family_member.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_demographics/familymembers.html'
                              , {'type': type, 'msg': msg, 'members': members})



def birthCertificates(request):
    type = "grid"
    dobs = gnuhealth_birth_certificate.objects.all()
    return render(request, 'health_demographics/birth_certificates.html'
                  , {'dobs': dobs
                  , 'type': type})

def addBirthCertificate(request):
    if request.method == "POST":
        form = birthCertificateForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_birth_certificate.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        #form.fields["id"].initial =  1
        id = request.POST['id']
        write_date = request.POST['write_date']
        write_uid = request.POST['write_uid']
        create_date = request.POST['create_date']
        create_uid = request.POST['create_uid']
        name = request.POST['name']
        father = None
        mother = None
        dob = request.POST['dob']
        code = request.POST['code']
        country = request.POST['country']
        country_subdivision = request.POST['country_subdivision']
        institution = None
        signed_by = None
        document_digest = request.POST['document_digest']
        certification_date = request.POST['certification_date']
        state = request.POST['state']
        observations = request.POST['observations']


        bcir = gnuhealth_birth_certificate(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,name=name,father=father,mother=mother,dob=dob,code=code,country=country,
        country_subdivision=country_subdivision,institution=institution,signed_by=signed_by,
        document_digest=document_digest,certification_date=certification_date,state=state,
        observations=observations)
        bcir.save()
        dobs = gnuhealth_birth_certificate.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_demographics/birth_certificates.html'
                              , {'type': type, 'msg': msg, 'dobs': dobs})
           # except:
            #    pass
       # else:                
        #    messages.error(request, f'Sorry, Record Save Error')
         #   return HttpResponse("Invalid Form.")
    else:
        form = birthCertificateForm()
        latest = gnuhealth_birth_certificate.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        #form.fields["id"].initial =  1
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
        return render(request, 'health_demographics/birth_certificates.html', {'type': type, 'form': form})


def editBirthCertificate(request, id):
    type = "edit"
    editForm = gnuhealth_birth_certificate.objects.get(id=id)
    return render(request, 'health_demographics/birth_certificates.html', {'form': editForm, 'type': type})


def updateBirthCertificate(request, id):
    type = "grid"
    order = gnuhealth_birth_certificate.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    order_id = order.id
    create_date = order.create_date
    write_date = order.write_date
    create_uid = order.create_uid
    write_uid = order.write_uid
    order = gnuhealth_birth_certificate(id=order_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    order.save()
    msg = "3"
    dobs = gnuhealth_birth_certificate.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_demographics/birth_certificates.html'
                       , {'type': type, 'msg': msg, 'dobs': dobs})


def deleteBirthCertificate(request, id):
    order = gnuhealth_birth_certificate.objects.get(id=id)
    ordery.delete()
    type = "grid"
    msg = "2"
    dobs = gnuhealth_birth_certificate.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_demographics/birth_certificates.html'
                              , {'type': type, 'msg': msg, 'dobs': dobs})

def deathCertificates(request):
    type = "grid"
    dods = gnuhealth_death_certificate.objects.all()
    return render(request, 'health_demographics/death_certificates.html'
                  , {'dods': dods
                  , 'type': type})

def addDeathCertificate(request):
    if request.method == "POST":
        form = deathCertificateForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        #latest = gnuhealth_death_certificate.objects.latest('id')
        #form.fields["id"].initial = latest.id + 1
        form.fields["id"].initial =  1
        id = request.POST['id']
        write_date = request.POST['write_date']
        write_uid = request.POST['write_uid']
        create_date = request.POST['create_date']
        create_uid = request.POST['create_uid']
        name = request.POST['name']
        father = None
        mother = None
        dob = request.POST['dob']
        code = request.POST['code']
        country = request.POST['country']
        country_subdivision = request.POST['country_subdivision']
        institution = None
        signed_by = None
        document_digest = request.POST['document_digest']
        certification_date = request.POST['certification_date']
        state = request.POST['state']
        observations = request.POST['observations']


        bcir = gnuhealth_birth_certificate(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,name=name,father=father,mother=mother,dob=dob,code=code,country=country,
        country_subdivision=country_subdivision,institution=institution,signed_by=signed_by,
        document_digest=document_digest,certification_date=certification_date,state=state,
        observations=observations)
        bcir.save()
        dods = gnuhealth_death_certificate.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_demographics/death_certificates.html'
                              , {'type': type, 'msg': msg, 'dods': dods})
           # except:
            #    pass
       # else:                
        #    messages.error(request, f'Sorry, Record Save Error')
         #   return HttpResponse("Invalid Form.")
    else:
        form = deathCertificateForm()
        #latest = gnuhealth_death_certificate.objects.latest('id')
        #form.fields["id"].initial = latest.id + 1
        form.fields["id"].initial =  1
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
        return render(request, 'health_demographics/death_certificates.html', {'type': type, 'form': form})


def editDeathCertificate(request, id):
    type = "edit"
    editForm = gnuhealth_death_certificate.objects.get(id=id)
    return render(request, 'health_demographics/death_certificates.html', {'form': editForm, 'type': type})


def updateDeathCertificate(request, id):
    type = "grid"
    dod = gnuhealth_death_certificate.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    order_id = order.id
    create_date = order.create_date
    write_date = order.write_date
    create_uid = order.create_uid
    write_uid = order.write_uid
    dod = gnuhealth_death_certificate(id=order_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    dod.save()
    msg = "3"
    dods = gnuhealth_death_certificate.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_demographics/death_certificates.html'
                       , {'type': type, 'msg': msg, 'dods': dods})


def deleteDeathCertificate(request, id):
    dod = gnuhealth_death_certificate.objects.get(id=id)
    dod.delete()
    type = "grid"
    msg = "2"
    dods = gnuhealth_death_certificate.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_demographics/death_certificates.html'
                              , {'type': type, 'msg': msg, 'dods': dods})


def du(request):
    type = "grid"
    dus = gnuhealth_du.objects.all()
    return render(request, 'health_demographics/dus.html'
                  , {'dus': dus
                  , 'type': type})

def addDu(request):
    if request.method == "POST":
        form = duForm(request.POST)
      #  if form.is_valid():
          #  try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_du.objects.latest('id')
        form.fields["id"].initial = 2
        id = request.POST['id']
        address_city = request.POST['address_city']
        address_country = request.POST['address_country']
        address_city = request.POST['address_city']
        address_district = request.POST['address_district']
        address_municipality = request.POST['address_municipality']
        address_street = request.POST['address_street']
        address_street_bis = request.POST['address_street_bis']
        address_street_number = request.POST['address_street_number']
        address_subdivision = request.POST['address_subdivision']
        address_zip = request.POST['address_zip']
        altitude = request.POST['altitude']
        bathrooms = request.POST['bathrooms']
        bedrooms = request.POST['bedrooms']
        create_date = request.POST['create_date']
        create_uid = request.POST['create_uid']
        desc = request.POST['desc']
        dwelling = request.POST['dwelling']
        electricity = True
        gas = True
        housing = request.POST['housing']
        internet = True
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        materials = request.POST['materials']
        name = request.POST['name']
        operational_sector = request.POST['operational_sector']
        #picture = request.POST['picture']
        roof_type = request.POST['roof_type']
        sewers = True
        telephone = True
        television = True
        total_surface = request.POST['total_surface']
        trash = True
        urladdr = request.POST['urladdr']
        water = True
        write_date = request.POST['write_date']
        write_uid = request.POST['write_uid']

        du = gnuhealth_du(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, water=water, urladdr=urladdr,trash=trash,
                              total_surface=total_surface, telephone=telephone,television=television,
                              sewers=sewers, roof_type=roof_type, picture='', operational_sector=operational_sector,
                              name=name , materials=materials, longitude=longitude, latitude=latitude,
                              internet=internet, housing=housing, gas=gas, electricity=electricity, dwelling=dwelling,
                              desc=desc,bedrooms=bedrooms, bathrooms=bathrooms, altitude=altitude,
                              address_city = address_city,address_country = address_country,
        address_district = address_district,address_municipality = address_municipality,address_street = address_street,
        address_street_bis = address_street_bis,
        address_street_number = address_street_number,
        address_subdivision = address_subdivision,
        address_zip = address_zip)
        du.save()
        dus = gnuhealth_du.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_demographics/dus.html'
                              , {'type': type, 'msg': msg, 'dus': dus})
          #  except:
           #     pass
       # else:                
        #    messages.error(request, f'Sorry, Record Save Error')
         #   return HttpResponse("Invalid Form.")
    else:
        form = duForm()
        latest = gnuhealth_family.objects.latest('id')
        form.fields["id"].initial = 2
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
        return render(request, 'health_demographics/dus.html', {'type': type, 'form': form})


def editDu(request, id):
    type = "edit"
    editForm = gnuhealth_du.objects.get(id=id)
    return render(request, 'health_demographics/dus.html', {'form': editForm, 'type': type})


def updateDu(request, id):
    type = "grid"
    du = gnuhealth_du.objects.get(id=id)
    id = request.POST['id']
    address_city = request.POST['address_city']
    address_country = request.POST['address_country']
    address_city = request.POST['address_city']
    address_district = request.POST['address_district']
    address_municipality = request.POST['address_municipality']
    address_street = request.POST['address_street']
    address_street_bis = request.POST['address_street_bis']
    address_street_number = request.POST['address_street_number']
    address_subdivision = request.POST['address_subdivision']
    address_zip = request.POST['address_zip']
    altitude = request.POST['altitude']
    bathrooms = request.POST['bathrooms']
    bedrooms = request.POST['bedrooms']
    create_date = request.POST['create_date']
    create_uid = request.POST['create_uid']
    desc = request.POST['desc']
    dwelling = request.POST['dwelling']
    electricity = True
    gas = True
    housing = request.POST['housing']
    internet = True
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    latitude = request.POST['latitude']
    materials = request.POST['materials']
    name = request.POST['name']
    operational_sector = request.POST['operational_sector']
    #picture = request.POST['picture']
    roof_type = request.POST['roof_type']
    sewers = True
    telephone = True
    television = True
    total_surface = request.POST['total_surface']
    trash = True
    urladdr = request.POST['urladdr']
    water = True
    write_date = request.POST['write_date']
    write_uid = request.POST['write_uid']

    du = gnuhealth_du(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, water=water, urladdr=urladdr,trash=trash,
                              total_surface=total_surface, telephone=telephone,television=television,
                              sewers=sewers, roof_type=roof_type, picture='', operational_sector=operational_sector,
                              name=name , materials=materials, longitude=longitude, latitude=latitude,
                              internet=internet, housing=housing, gas=gas, electricity=electricity, dwelling=dwelling,
                              desc=desc,bedrooms=bedrooms, bathrooms=bathrooms, altitude=altitude,
                              address_city = address_city,address_country = address_country,
        address_district = address_district,address_municipality = address_municipality,address_street = address_street,
        address_street_bis = address_street_bis,
        address_street_number = address_street_number,
        address_subdivision = address_subdivision,
        address_zip = address_zip)
    du.save()
    msg = "3"
    dus = gnuhealth_du.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_demographics/dus.html'
                       , {'type': type, 'msg': msg, 'dus': dus})


def deleteDu(request, id):
    du = gnuhealth_du.objects.get(id=id)
    du.delete()
    type = "grid"
    msg = "2"
    dus = gnuhealth_du.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_demographics/dus.html'
                              , {'type': type, 'msg': msg, 'dus': dus})

def searchCountry(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    countries = country_country.objects.filter(name__startswith=search_text.capitalize())

    if len(countries) == 0:
        countries = country_country.objects.filter(id=search_text)

    return render_to_response('health_demographics/js/ajax-search.html', {'countries': countries})

def searchOpsector(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    opsectors = gnuhealth_operational_sector.objects.filter(name__startswith=search_text.capitalize())

    if len(opsectors) == 0:
        opsectors = gnuhealth_operational_sector.objects.filter(id=search_text)

    return render_to_response('health_demographics/js/ajax-search.html', {'opsectors': opsectors})



def searchSubdiv(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    subdivs = country_subdivision.objects.filter(name__startswith=search_text.capitalize())

    if len(subdivs) == 0:
        subdivs = country_subdivision.objects.filter(id=search_text)

    return render_to_response('health_demographics/js/ajax-search.html', {'subdivs': subdivs})
