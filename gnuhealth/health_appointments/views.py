from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from health_appointments.models import *
from health_appointments.forms import *

from django.contrib import messages
# Create your views here.
def index(request):
    type = "grid"
    appointments = gnuhealth_appointment.objects.all()
    return render(request, 'health_appointments/appointments.html'
                  , {'appointments': appointments
                  , 'type': type})
  
def appointments(request):
    type = "grid"
    appointments = gnuhealth_appointment.objects.all()
    return render(request, 'health_appointments/appointments.html'
                  , {'appointments': appointments
                  , 'type': type})
    
def addAppointment(request):
    if request.method == "POST":
        form = appointmentForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_appointment.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
                #form.fields["id"].initial =  1
        id = request.POST['id']
        appointment_date = request.POST['appointment_date']
        appointment_type = request.POST['appointment_type']
        checked_in_date = None
        comments = request.POST['comments']
        consultations = None
        healthprof = request.POST['healthprof']
        institution = request.POST['institution']
        name = None
        patient = request.POST['patient']
        speciality = None
        state = request.POST['state']
        urgency = request.POST['urgency']
        visit_type = request.POST['visit_type']
        appointment_date_end = request.POST['appointment_date_end']
        event = None
        inpatient_registration_code = None
        create_date = request.POST['create_date']
        write_date = request.POST['write_date']
        create_uid = request.POST['create_uid']
        write_uid = request.POST['write_uid']
        app = gnuhealth_appointment(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, inpatient_registration_code=inpatient_registration_code,
                               event=event, appointment_date_end=appointment_date_end,
                               visit_type=visit_type,urgency=urgency,state=state,speciality=speciality,patient=patient,
                               institution=institution,healthprof=healthprof,consultations=consultations,
                               comments=comments,checked_in_date=checked_in_date,appointment_type=appointment_type,
                               appointment_date=appointment_date)
        app.save()
        appointments = gnuhealth_appointment.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_appointments/appointments.html'
                              , {'type': type, 'msg': msg, 'appointments': appointments})
         #   except:
          #      pass
        #else:                
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = appointmentForm()
        latest = gnuhealth_appointment.objects.latest('id')
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
        return render(request, 'health_appointments/appointments.html', {'type': type, 'form': form})


def editAppointment(request, id):
    type = "edit"
    editForm = gnuhealth_appointment.objects.get(id=id)
    return render(request, 'health_appointments/appointments.html', {'form': editForm, 'type': type})


def updateAppointment(request, id):
    type = "grid"
    app = gnuhealth_appointment.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    app_id = app.id
    create_date = app.create_date
    write_date = app.write_date
    create_uid = app.create_uid
    write_uid = app.write_uid
    app = gnuhealth_appointment(id=app_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    app.save()
    msg = "3"
    appointments = gnuhealth_appointment.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_appointment/appointments.html'
                       , {'type': type, 'msg': msg, 'appointments': appointments})


def deleteAppointment(request, id):
    appointment = gnuhealth_appointment.objects.get(id=id)
    appointment.delete()
    type = "grid"
    msg = "2"
    appointments = gnuhealth_appointment.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_appointments/appointments.html'
                              , {'type': type, 'msg': msg, 'appointments': appointments})

