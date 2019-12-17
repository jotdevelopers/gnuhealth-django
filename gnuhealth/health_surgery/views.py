from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_surgery.models import *
from health_party.models import *
from health_demographics.forms import *
from health_surgery.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request, 'health_surgery/index.html')

def surgeries(request):
    type = "grid"
    surgeries = gnuhealth_surgery.objects.all()
    return render(request, 'health_surgery/surgeries.html'
                  , {'surgeries': surgeries
                      , 'type': type})


def addSurgery(request):
    if request.method == "POST":
        form = surgeryForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_surgery.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                surgeries = gnuhealth_surgery.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_surgery/surgeries.html'
                              , {'type': type, 'msg': msg, 'surgeries': surgeries})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = surgeryForm()
        latest = gnuhealth_surgery.objects.latest('id')
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
        return render(request, 'health_surgery/surgeries.html', {'type': type, 'form': form})


def editSurgery(request, id):
    type = "edit"
    editForm = gnuhealth_surgery.objects.get(id=id)
    return render(request, 'health_surgery/surgeries.html', {'form': editForm, 'type': type})


def updateSurgery(request, id):
    type = "grid"
    eth = gnuhealth_surgery.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_surgery(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    eth.save()
    msg = "3"
    surgeries = gnuhealth_surgery.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_surgery/surgeries.html'
                  , {'type': type, 'msg': msg, 'surgeries': surgeries})


def deleteSurgery(request, id):
    surgery = gnuhealth_surgery.objects.get(id=id)
    surgery.delete()
    type = "grid"
    msg = "2"
    surgeries = gnuhealth_surgery.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_surgery/surgeries.html'
                  , {'type': type, 'msg': msg, 'surgeries': surgeries})
