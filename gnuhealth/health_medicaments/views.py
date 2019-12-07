from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from health_medicaments.models import *
from health_medicaments.forms import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

# Medicaments module functions start
def medicament_main(request):
	return render(request, "health_medicaments/medicaments-medicament.html")

def medication_frequencies(request):
	return render(request, "health_medicaments/medicaments-medication-frequencies.html")
# Medicaments module functions end

def medicamentCategory(request):
    type = "grid"
    medicamentCategory = gnuhealth_medicament_category.objects.all()
    return render(request, 'health_medicaments/medicamentCategory.html',
                  {'medicamentCategory': medicamentCategory, 'type': type})


def addMedicamentCategory(request):
    if request.method == "POST":
        form = medicamentCategoryForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(medicamentCategory)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = medicamentCategoryForm()
        form.fields["id"].initial = gnuhealth_medicament_category.objects.count()+1
        type = "add"
        return render(request, 'health_medicaments/medicamentCategory.html', {'type': type, 'form': form})


def editMedicamentCategory(request, id):
    type = "edit"
    editForm = gnuhealth_medicament_category.objects.get(id=id)
    return render(request, 'health_medicaments/medicamentCategory.html', {'form': editForm, 'type': type})


def updateMedicamentCategory(request, id):
    type = "grid"
    temp = gnuhealth_medicament_category.objects.get(id=id)
    cat_id = temp.id
    name = request.POST['name']
    parent = request.POST['parent']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_medicament_category(id=cat_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, name=name,
                                                parent=parent)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(medicamentCategory)


def deleteMedicamentCategory(request, id):
    temp = gnuhealth_medicament_category.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(medicamentCategory)    

def drugForm(request):
    type = "grid"
    drugForm = gnuhealth_drug_form.objects.all()
    return render(request, 'health_medicaments/drugForm.html',
                  {'drugForm': drugForm, 'type': type})


def addDrugForm(request):
    if request.method == "POST":
        form = drugFormForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(drugForm)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = medicamentCategoryForm()
        form.fields["id"].initial = gnuhealth_drug_form.objects.count()+1
        type = "add"
        return render(request, 'health_medicaments/drugForm.html', {'type': type, 'form': form})


def editDrugForm(request, id):
    type = "edit"
    editForm = gnuhealth_drug_form.objects.get(id=id)
    return render(request, 'health_medicaments/drugForm.html', {'form': editForm, 'type': type})


def updateDrugForm(request, id):
    type = "grid"
    temp = gnuhealth_drug_form.objects.get(id=id)
    drf_id = temp.id
    code = request.POST['code']
    name = request.POST['name']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_drug_form(id=drf_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, code=code,
                                                name=name)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(drugForm)


def deleteDrugForm(request, id):
    temp = gnuhealth_drug_form.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(drugForm)    

def drugRoute(request):
    type = "grid"
    drugRoute = gnuhealth_drug_route.objects.all()
    return render(request, 'health_medicaments/drugRoute.html',
                  {'drugRoute': drugRoute, 'type': type})


def addDrugRoute(request):
    if request.method == "POST":
        form = drugRouteForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(drugRoute)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = drugRouteForm()
        form.fields["id"].initial = gnuhealth_drug_route.objects.count()+1
        type = "add"
        return render(request, 'health_medicaments/drugRoute.html', {'type': type, 'form': form})


def editDrugRoute(request, id):
    type = "edit"
    editForm = gnuhealth_drug_route.objects.get(id=id)
    return render(request, 'health_medicaments/drugRoute.html', {'form': editForm, 'type': type})


def updateDrugRoute(request, id):
    type = "grid"
    temp = gnuhealth_drug_route.objects.get(id=id)
    drr_id = temp.id
    code = request.POST['code']
    name = request.POST['name']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_drug_route(id=drr_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, code=code,
                                                name=name)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(drugRoute)


def deleteDrugRoute(request, id):
    temp = gnuhealth_drug_route.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(drugRoute)    

def doseUnit(request):
    type = "grid"
    doseUnit = gnuhealth_dose_unit.objects.all()
    return render(request, 'health_medicaments/doseUnit.html',
                  {'doseUnit': doseUnit, 'type': type})


def addDoseUnit(request):
    if request.method == "POST":
        form = doseUnitForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(doseUnit)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = doseUnitForm()
        form.fields["id"].initial = gnuhealth_dose_unit.objects.count()+1
        type = "add"
        return render(request, 'health_medicaments/doseUnit.html', {'type': type, 'form': form})


def editDoseUnit(request, id):
    type = "edit"
    editForm = gnuhealth_dose_unit.objects.get(id=id)
    return render(request, 'health_medicaments/doseUnit.html', {'form': editForm, 'type': type})


def updateDoseUnit(request, id):
    type = "grid"
    temp = gnuhealth_dose_unit.objects.get(id=id)
    dsu_id = temp.id
    desc = request.POST['desc']
    name = request.POST['name']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_dose_unit(id=dsu_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, desc=desc,
                                                name=name)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(doseUnit)


def deleteDoseUnit(request, id):
    temp = gnuhealth_dose_unit.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(doseUnit)    

def medicationDosage(request):
    type = "grid"
    medicationDosage = gnuhealth_medication_dosage.objects.all()
    return render(request, 'health_medicaments/medicationDosage.html',
                  {'medicationDosage': medicationDosage, 'type': type})


def addMedicationDosage(request):
    if request.method == "POST":
        form = medicationDosageForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(medicationDosage)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = medicationDosageForm()
        form.fields["id"].initial = gnuhealth_medication_dosage.objects.count()+1
        type = "add"
        return render(request, 'health_medicaments/medicationDosage.html', {'type': type, 'form': form})


def editMedicationDosage(request, id):
    type = "edit"
    editForm = gnuhealth_medication_dosage.objects.get(id=id)
    return render(request, 'health_medicaments/medicationDosage.html', {'form': editForm, 'type': type})


def updateMedicationDosage(request, id):
    type = "grid"
    temp = gnuhealth_medication_dosage.objects.get(id=id)
    mdo_id = temp.id
    abbreviation = request.POST['abbreviation']
    code = request.POST['code']
    name = request.POST['name']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_medication_dosage(id=mdo_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, code=code,
                                                name=name, abbreviation=abbreviation)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(medicationDosage)


def deleteMedicationDosage(request, id):
    temp = gnuhealth_medication_dosage.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(medicationDosage)    

def medicament(request):
    type = "grid"
    medicament = gnuhealth_medicament.objects.all()
    return render(request, 'health_medicaments/medicament.html',
                  {'medicament': medicament, 'type': type})


def addMedicament(request):
    if request.method == "POST":
        form = medicamentForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(medicament)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = medicamentForm()
        form.fields["id"].initial = gnuhealth_medicament.objects.count()+1
        type = "add"
        return render(request, 'health_medicaments/medicament.html', {'type': type, 'form': form})


def editMedicament(request, id):
    type = "edit"
    editForm = gnuhealth_medicament.objects.get(id=id)
    return render(request, 'health_medicaments/medicament.html', {'form': editForm, 'type': type})


def updateMedicament(request, id):
    type = "grid"
    temp = gnuhealth_medicament.objects.get(id=id)
    med_id = temp.id
    active = request.POST['active']
    active_component = request.POST['active_component']
    adverse_reaction = request.POST['adverse_reaction']
    category = request.POST['category']
    composition = request.POST['composition']
    dosage = request.POST['dosage']
    form = request.POST['form']
    indications = request.POST['indications']
    is_vaccine = request.POST['is_vaccine']
    name = request.POST['name']
    notes = request.POST['notes']
    overdosage = request.POST['overdosage']
    pregnancy = request.POST['pregnancy']
    pregnancy_category = request.POST['pregnancy_category']
    pregnancy_warning = request.POST['pregnancy_warning']
    presentation = request.POST['presentation']
    route = request.POST['route']
    sol_conc = request.POST['sol_conc']
    sol_conc_unit = request.POST['sol_conc_unit']
    sol_vol = request.POST['sol_vol']
    sol_vol_unit = request.POST['sol_vol_unit']
    storage = request.POST['storage']
    strength = request.POST['strength']
    therapeutic_action = request.POST['therapeutic_action']
    unit = request.POST['unit']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_medicament(id=med_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, active=active,
                                                active_component=active_component, adverse_reaction=adverse_reaction,
                                                category=category, composition=composition, dosage=dosage, form=form,
                                                indications=indications, is_vaccine=is_vaccine, name=name,
                                                notes=notes, overdosage=overdosage, pregnancy=pregnancy,
                                                pregnancy_category=pregnancy_category, pregnancy_warning=pregnancy_warning,
                                                presentation=presentation, route=route, sol_conc=sol_conc,
                                                sol_conc_unit=sol_conc_unit, sol_vol=sol_vol, sol_vol_unit=sol_vol_unit,
                                                storage=storage, strength=strength, therapeutic_action=therapeutic_action,
                                                unit=unit)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(medicament)


def deleteMedicament(request, id):
    temp = gnuhealth_medicament.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(medicament)