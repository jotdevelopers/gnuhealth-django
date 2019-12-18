from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_configuration.models import *
from health_prescriptions.models import *
from health_prescriptions.forms import *
from health_configuration.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def prescriptions(request):
    type = "grid"
    prescriptions = gnuhealth_prescription_order.objects.all()
    return render(request, 'health_prescriptions/prescriptions.html'
                  , {'prescriptions': prescriptions
                      , 'type': type})


def addPrescription(request):
    if request.method == "POST":
        form = prescriptionForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
                #latest = gnuhealth_prescription_order.objects.latest('id')
        form.fields["id"].initial =  1

        id = request.POST['id']
        create_date = request.POST['create_date']
        write_date = request.POST['write_date']
        create_uid = request.POST['create_uid']
        write_uid = request.POST['write_uid']
        healthprof = request.POST['healthprof']
        notes = request.POST['notes']
        patient = 1
        pharmacy = None
        pregnancy_warning = False
        prescription_date = request.POST['prescription_date']
        prescription_id = request.POST['prescription_id']
        prescription_warning_ack = True
        state = request.POST['state']
        user_id = None
        digital_signature = request.POST['digital_signature']
        document_digest = request.POST['document_digest']
        serializer = None
        service = None
        pres = gnuhealth_prescription_order(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid,
                              healthprof = healthprof,
        notes = notes,
        patient = patient,
        pharmacy = pharmacy,
        pregnancy_warning = pregnancy_warning,
        prescription_date = prescription_date,
        prescription_id = prescription_id,
        prescription_warning_ack = prescription_warning_ack,
        state = state,
        user_id = user_id,
        digital_signature = digital_signature,
        document_digest = document_digest,
        serializer = serializer,
        service = service)
        pres.save()
        prescriptions = gnuhealth_prescription_order.objects.all()
        
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_prescriptions/prescriptions.html'
                              , {'type': type, 'msg': msg, 'prescriptions': prescriptions})
            #except:
             #   pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = prescriptionForm()
        #latest = gnuhealth_prescription_order.objects.latest('id')
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
        return render(request, 'health_prescriptions/prescriptions.html', {'type': type, 'form': form})


def editPrescription(request, id):
    type = "edit"
    editForm = gnuhealth_prescription_order.objects.get(id=id)
    return render(request, 'health_prescriptions/prescriptions.html', {'form': editForm, 'type': type})


def updatePrescription(request, id):
    type = "grid"
    pres = gnuhealth_prescription_order.objects.get(id=id)
    id = request.POST['id']
    create_date = request.POST['create_date']
    write_date = request.POST['write_date']
    create_uid = request.POST['create_uid']
    write_uid = request.POST['write_uid']
    healthprof = request.POST['healthprof']
    notes = request.POST['notes']
    patient = 1
    pharmacy = None
    pregnancy_warning = False
    prescription_date = request.POST['prescription_date']
    prescription_id = request.POST['prescription_id']
    prescription_warning_ack = True
    state = request.POST['state']
    user_id = None
    digital_signature = request.POST['digital_signature']
    document_digest = request.POST['document_digest']
    serializer = None
    service = None
    pres = gnuhealth_prescription_order(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid,
                              healthprof = healthprof,
        notes = notes,
        patient = patient,
        pharmacy = pharmacy,
        pregnancy_warning = pregnancy_warning,
        prescription_date = prescription_date,
        prescription_id = prescription_id,
        prescription_warning_ack = prescription_warning_ack,
        state = state,
        user_id = user_id,
        digital_signature = digital_signature,
        document_digest = document_digest,
        serializer = serializer,
        service = service)
    pres.save()
    msg = "3"
    prescriptions = gnuhealth_prescription_order.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_prescriptions/prescriptions.html'
                  , {'type': type, 'msg': msg, 'prescriptions': prescriptions})


def deletePrescription(request, id):
    prescription = gnuhealth_prescription_order.objects.get(id=id)
    prescription.delete()
    type = "grid"
    msg = "2"
    prescriptions = gnuhealth_prescription_order.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_prescriptions/prescriptions.html'
                  , {'type': type, 'msg': msg, 'prescriptions': prscriptions})
