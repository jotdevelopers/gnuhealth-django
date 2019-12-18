from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from health_lab.models import *
from health_lab.forms import *
# Create your views here.

def index(request):
    return HttpResponse("Hello")

# def addlabtestrequest(request):
#     return render(request,'health_lab/add-lab-test-request.html') #,{'form':form})  

# def labtestresult(request):
#     return render(request, 'health_lab/lab-test-results.html')

    

# # Laboratory module functions start
# def lab_test_types(request):
# 	return render(request, "health_laboratory/laboratory-lab-test-types.html")

# def lab_test_units(request):
# 	return render(request, "health_laboratory/laboratory-lab-test-units.html")
# # Laboratory module functions end


def labRequests(request):
    type = "grid"
    ethnicities = gnuhealth_lab.objects.all()
    return render(request, 'health_lab/lab_test_requests.html'
                  , {'ethnicities': ethnicities
                      , 'type': type})


def addLabRequest(request):
    if request.method == "POST":
        form = requestLabForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_ethnicity.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                ethnicities = gnuhealth_ethnicity.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/patients/ethnicities.html'
                              , {'type': type, 'msg': msg, 'ethnicities': ethnicities})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = requestLabForm()
        latest = gnuhealth_ethnicity.objects.latest('id')
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
        return render(request, 'health_configuration/patients/ethnicities.html', {'type': type, 'form': form})


def editLabRequest(request, id):
    type = "edit"
    editForm = gnuhealth_ethnicity.objects.get(id=id)
    return render(request, 'health_configuration/patients/ethnicities.html', {'form': editForm, 'type': type})


def updateLabRequest(request, id):
    type = "grid"
    eth = gnuhealth_ethnicity.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_ethnicity(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    eth.save()
    msg = "3"
    ethnicities = gnuhealth_ethnicity.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/patients/ethnicities.html'
                  , {'type': type, 'msg': msg, 'ethnicities': ethnicities})


def deleteLabRequest(request, id):
    ethnicity = gnuhealth_ethnicity.objects.get(id=id)
    ethnicity.delete()
    type = "grid"
    msg = "2"
    ethnicities = gnuhealth_ethnicity.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/patients/ethnicities.html'
                  , {'type': type, 'msg': msg, 'ethnicities': ethnicities})


def labResults(request):
    type = "grid"
    ethnicities = gnuhealth_ethnicity.objects.all()
    return render(request, 'health_configuration/patients/ethnicities.html'
                  , {'ethnicities': ethnicities
                      , 'type': type})


def addLabResult(request):
    if request.method == "POST":
        form = ethnicityForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_ethnicity.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                ethnicities = gnuhealth_ethnicity.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_configuration/patients/ethnicities.html'
                              , {'type': type, 'msg': msg, 'ethnicities': ethnicities})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = ethnicityForm()
        latest = gnuhealth_ethnicity.objects.latest('id')
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
        return render(request, 'health_configuration/patients/ethnicities.html', {'type': type, 'form': form})


def editLabResult(request, id):
    type = "edit"
    editForm = gnuhealth_ethnicity.objects.get(id=id)
    return render(request, 'health_configuration/patients/ethnicities.html', {'form': editForm, 'type': type})


def updateLabResult(request, id):
    type = "grid"
    eth = gnuhealth_ethnicity.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_ethnicity(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    eth.save()
    msg = "3"
    ethnicities = gnuhealth_ethnicity.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_configuration/patients/ethnicities.html'
                  , {'type': type, 'msg': msg, 'ethnicities': ethnicities})


def deleteLabResult(request, id):
    ethnicity = gnuhealth_ethnicity.objects.get(id=id)
    ethnicity.delete()
    type = "grid"
    msg = "2"
    ethnicities = gnuhealth_ethnicity.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_configuration/patients/ethnicities.html'
                  , {'type': type, 'msg': msg, 'ethnicities': ethnicities})




def labTestUnits(request):
    type = "grid"
    labTestUnits = gnuhealth_lab_test_units.objects.all()
    return render(request, 'health_lab/labTestUnits.html',
                  {'labTestUnits': labTestUnits, 'type': type, 'selected': 'Lab Test Units'})


def addLabTestUnits(request):
    if request.method == "POST":
        form = labTestUnitsForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(labTestUnits)
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addLabTestUnits)
    else:
        form = labTestUnitsForm()
        form.fields["id"].initial = gnuhealth_lab_test_units.objects.count()+1
        type = "add"
        return render(request, 'health_lab/labTestUnits.html', {'type': type, 'form': form, 'selected': 'Lab Test Units'})


def editLabTestUnits(request, id):
    type = "edit"
    editForm = gnuhealth_lab_test_units.objects.get(id=id)
    return render(request, 'health_lab/labTestUnits.html', {'form': editForm, 'type': type, 'selected': 'Lab Test Units'})


def updateLabTestUnits(request, id):
    type = "grid"
    temp = gnuhealth_lab_test_units.objects.get(id=id)
    ltu_id = temp.id
    code = request.POST['code']
    name = request.POST['name']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_lab_test_units(id=ltu_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, name=name,
                                                code=code)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(labTestUnits)


def deleteLabTestUnits(request, id):
    temp = gnuhealth_lab_test_units.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(labTestUnits)


def labTestType(request):
	type = "grid"
	labTestType = gnuhealth_lab_test_type.objects.all()
	return render(request, 'health_lab/labTestType.html',
	              {'labTestType': labTestType, 'type': type, 'selected': 'Lab Test Types'})


def addLabTestType(request):
    if request.method == "POST":
        form = labTestTypeForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(labTestType)
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(addLabTestType)
    else:
        form = labTestTypeForm()
        form.fields["id"].initial = gnuhealth_lab_test_type.objects.count()+1
        type = "add"
        return render(request, 'health_lab/labTestType.html', {'type': type, 'form': form, 'selected': 'Lab Test Types'})


def editLabTestType(request, id):
    type = "edit"
    editForm = gnuhealth_lab_test_type.objects.get(id=id)
    return render(request, 'health_lab/labTestType.html', {'form': editForm, 'type': type, 'selected': 'Lab Test Types'})


def updateLabTestType(request, id):
    type = "grid"
    temp = gnuhealth_lab_test_type.objects.get(id=id)
    ltt_id = temp.id
    active = request.POST['active']
    code = request.POST['code']
    info = request.POST['info']
    name = request.POST['name']
    product_id = request.POST['product_id']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_lab_test_type(id=ltt_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, name=name,
                                                code=code, active=active, info=info, product_id=product_id)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(labTestType)


def deleteLabTestType(request, id):
    temp = gnuhealth_lab_test_type.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(labTestType)
