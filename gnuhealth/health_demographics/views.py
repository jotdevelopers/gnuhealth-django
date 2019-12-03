from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from health_demographics.models import *
from health_demographics.forms import *
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_configuration.models import *
from health_party.models import *
from health_configuration.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt



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
    families = gnuhealth_family.objects.all()
    return render(request, 'health_demographics/families.html'
                  , {'families': families
                  , 'type': type})

def addFamilyMember(request):
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


def editFamilyMember(request, id):
    type = "edit"
    editForm = gnuhealth_family.objects.get(id=id)
    return render(request, 'health_demographics/families.html', {'form': editForm, 'type': type})


def updateFamilyMember(request, id):
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


def deleteFamilyMember(request, id):
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



def birthCertificates(request):
    type = "grid"
    bods = gnuhealth_inpatient_meal_order.objects.all()
    return render(request, 'health_demographics/birth_certificates.html'
                  , {'orders': orders
                  , 'type': type})

def addBirthCertificate(request):
    if request.method == "POST":
        form = mealOrderForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_inpatient_meal_order.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                orders = gnuhealth_inpatient_meal_order.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_demographics/birth_certificates.html'
                              , {'type': type, 'msg': msg, 'orders': orders})
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = mealOrderForm()
        latest = gnuhealth_inpatient_meal_order.objects.latest('id')
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
        return render(request, 'health_demographics/birth_certificates.html', {'type': type, 'form': form})


def editBirthCertificate(request, id):
    type = "edit"
    editForm = gnuhealth_inpatient_meal_order.objects.get(id=id)
    return render(request, 'health_demographics/birth_certificates.html', {'form': editForm, 'type': type})


def updateBirthCertificate(request, id):
    type = "grid"
    order = gnuhealth_inpatient_meal_order.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    order_id = order.id
    create_date = order.create_date
    write_date = order.write_date
    create_uid = order.create_uid
    write_uid = order.write_uid
    order = gnuhealth_inpatient_meal_order(id=order_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    order.save()
    msg = "3"
    orders = gnuhealth_inpatient_meal_order.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_demographics/birth_certificates.html'
                       , {'type': type, 'msg': msg, 'orders': orders})


def deleteBirthCertificate(request, id):
    order = gnuhealth_inpatient_meal_order.objects.get(id=id)
    ordery.delete()
    type = "grid"
    msg = "2"
    orders = gnuhealth_inpatient_meal_order.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_demographics/birth_certificates.html'
                              , {'type': type, 'msg': msg, 'orders': orders})


def du(request):
    type = "grid"
    dus = gnuhealth_du.objects.all()
    return render(request, 'health_demographics/dus.html'
                  , {'dus': dus
                  , 'type': type})

def addDu(request):
    if request.method == "POST":
        form = duForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_du.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                dus = gnuhealth_du.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_demographics/dus.html'
                              , {'type': type, 'msg': msg, 'dus': dus})
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = duForm()
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
        return render(request, 'health_demographics/dus.html', {'type': type, 'form': form})


def editDu(request, id):
    type = "edit"
    editForm = gnuhealth_du.objects.get(id=id)
    return render(request, 'health_demographics/dus.html', {'form': editForm, 'type': type})


def updateDu(request, id):
    type = "grid"
    eth = gnuhealth_du.objects.get(id=id)
    name = request.POST['name']
    info = request.POST['info']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_du(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, info=info)
    eth.save()
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

    if len(countries) == 0:
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
