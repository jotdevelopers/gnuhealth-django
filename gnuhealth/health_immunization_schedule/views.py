from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from health_immunization_schedule.models import *
from health_immunization_schedule.forms import *


def immunizationSchedule(request):
    type = "grid"
    immunizationSchedules = gnuhealth_immunization_schedule.objects.order_by('id')[:200]
    return render(request, 'health_immunization/immunizationSchedule.html',
                  {'immunizationSchedules': immunizationSchedules, 'type': type, 'selected': 'Schedule Vaccines'})


def addImmunizationSchedule(request):
    if request.method == "POST":
        form = immunizationScheduleForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(immunizationSchedule)
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addImmunizationSchedule)
    else:
        form = immunizationScheduleForm()
        form.fields["id"].initial = gnuhealth_immunization_schedule.objects.count()+1
        type = "add"
        return render(request, 'health_immunization/immunizationSchedule.html', {'type': type, 'form': form, 'selected': 'Schedule Vaccines'})


def editImmunizationSchedule(request, id):
    type = "edit"
    editForm = gnuhealth_immunization_schedule.objects.get(id=id)
    return render(request, 'health_immunization/immunizationSchedule.html', {'form': editForm, 'type': type, 'selected': 'Schedule Vaccines'})


def updateImmunizationSchedule(request, id):
    type = "grid"
    temp = gnuhealth_immunization_schedule.objects.get(id=id)
    imu_id = temp.id
    country = request.POST['country']
    sched = request.POST['sched']
    desc = request.POST['desc']
    year = request.POST['year']
    active = request.POST['active']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_immunization_schedule(id=imu_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, country=country,
                                                sched=sched, year=year, active=active, desc=desc)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(immunizationSchedule)


def deleteImmunizationSchedule(request, id):
    temp = gnuhealth_immunization_schedule.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(immunizationSchedule)


def vaccineDoses(request):
    type = "grid"
    vaccineDoses = gnuhealth_immunization_schedule_dose.objects.all()
    return render(request, 'health_immunization/vaccineDoses.html',
                  {'vaccineDoses': vaccineDoses, 'type': type, 'selected': 'Vaccine Doses'})


def addVaccineDoses(request):
    if request.method == "POST":
        form = vaccineDosesForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(vaccineDoses)
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addVaccineDoses)
    else:
        form = vaccineDosesForm()
        form.fields["id"].initial = gnuhealth_immunization_schedule_dose.objects.count()+1
        type = "add"
        return render(request, 'health_immunization/vaccineDoses.html', {'type': type, 'form': form, 'selected': 'Vaccine Doses'})


def editVaccineDoses(request, id):
    type = "edit"
    editForm = gnuhealth_immunization_schedule_dose.objects.get(id=id)
    return render(request, 'health_immunization/vaccineDoses.html', {'form': editForm, 'type': type, 'selected': 'Vaccine Doses'})


def updateVaccineDoses(request, id):
    type = "grid"
    temp = gnuhealth_immunization_schedule_dose.objects.get(id=id)
    vac_id = temp.id

    age_dose = request.POST['age_dose']
    age_unit = request.POST['age_unit']
    dose_number = request.POST['dose_number']
    remarks = request.POST['remarks']
    vaccine = request.POST['vaccine']

    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid

    temp = gnuhealth_immunization_schedule_dose(id=vac_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, age_dose=age_dose,
                                                age_unit=age_unit, dose_number=dose_number, remarks=remarks, vaccine=vaccine)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(vaccineDoses)


def deleteVaccineDoses(request, id):
    temp = gnuhealth_immunization_schedule_dose.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(vaccineDoses)


def scheduleLine(request):
    type = "grid"
    scheduleLine = gnuhealth_immunization_schedule_line.objects.all()
    return render(request, 'health_immunization/scheduleLine.html',
                  {'scheduleLine': scheduleLine, 'type': type, 'selected': 'Schedule Line'})


def addScheduleLine(request):
    if request.method == "POST":
        form = scheduleLineForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(scheduleLine)
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addScheduleLine)
    else:
        form = scheduleLineForm()
        form.fields["id"].initial = gnuhealth_immunization_schedule_line.objects.count()+1
        type = "add"
        return render(request, 'health_immunization/scheduleLine.html', {'type': type, 'form': form, 'selected': 'Schedule Line'})


def editScheduleLine(request, id):
    type = "edit"
    editForm = gnuhealth_immunization_schedule_line.objects.get(id=id)
    return render(request, 'health_immunization/scheduleLine.html', {'form': editForm, 'type': type, 'selected': 'Schedule Line'})


def updateScheduleLine(request, id):
    type = "grid"
    temp = gnuhealth_immunization_schedule_line.objects.get(id=id)
    lin_id = temp.id

    remarks = request.POST['remarks']
    sched = request.POST['sched']
    scope = request.POST['scope']
    vaccine = request.POST['vaccine']

    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid

    temp = gnuhealth_immunization_schedule_line(id=lin_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, remarks=remarks,
                                                sched=sched, scope=scope, vaccine=vaccine)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(scheduleLine)


def deleteScheduleLine(request, id):
    temp = gnuhealth_immunization_schedule_line.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(scheduleLine)
