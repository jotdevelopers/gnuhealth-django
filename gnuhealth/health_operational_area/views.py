from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from health_operational_area.models import *
from health_operational_area.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response


# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

def operationalSectors(request):
    type = "grid"
    opsectors = gnuhealth_operational_sector.objects.all()
    return render(request, 'health_operational_area/operational_sectors.html'
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
                return render(request, 'health_operational_area/operational_sectors.html'
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
        return render(request, 'health_operational_area/operational_sectors.html', {'type': type, 'form': form})


def editOperationalSector(request, id):
    type = "edit"
    editForm = gnuhealth_operational_sector.objects.get(id=id)
    return render(request, 'health_operational_area/operational_sectors.html', {'form': editForm, 'type': type})


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


    return render(request, 'health_operational_area/operational_sectors.html'
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

    return render(request, 'health_operational_area/operational_sectors.html'
                              , {'type': type, 'msg': msg, 'opsectors': opsectors})

def operationalAreas(request):
    type = "grid"
    opareas = gnuhealth_operational_area.objects.all()
    return render(request, 'health_operational_area/operational_areas.html'
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
                return render(request, 'health_operational_area/operational_areas.html'
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
        return render(request, 'health_operational_area/operational_areas.html', {'type': type, 'form': form})


def editOperationalArea(request, id):
    type = "edit"
    editForm = gnuhealth_operational_area.objects.get(id=id)
    return render(request, 'health_operational_area/operational_areas.html', {'form': editForm, 'type': type})


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


    return render(request, 'health_operational_area/operational_areas.html'
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

    return render(request, 'health_operational_area/operational_areas.html'
                              , {'type': type, 'msg': msg, 'opareas': opareas})

def searchOperationalArea(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    operationalareas = gnuhealth_operational_area.objects.filter(name__startswith=search_text.capitalize())

    if len(operationalareas) == 0:
        operationalareas = gnuhealth_operational_area.objects.filter(id=search_text)

    return render_to_response('health_operational_area/js/ajax-search.html', {'operationalareas': operationalareas})

