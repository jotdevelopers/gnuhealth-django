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


def labTestUnits(request):
    type = "grid"
    labTestUnits = gnuhealth_lab_test_units.objects.all()
    return render(request, 'health_lab/labTestUnits.html',
                  {'labTestUnits': labTestUnits, 'type': type})


def addLabTestUnits(request):
    if request.method == "POST":
        form = labTestUnitsForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(labTestUnits)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = labTestUnitsForm()
        form.fields["id"].initial = gnuhealth_lab_test_units.objects.count()+1
        type = "add"
        return render(request, 'health_lab/labTestUnits.html', {'type': type, 'form': form})


def editLabTestUnits(request, id):
    type = "edit"
    editForm = gnuhealth_lab_test_units.objects.get(id=id)
    return render(request, 'health_lab/labTestUnits.html', {'form': editForm, 'type': type})


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
	              {'labTestType': labTestType, 'type': type})


def addLabTestType(request):
    if request.method == "POST":
        form = labTestTypeForm(request.POST)
        if form.is_valid():
	        type = "grid"
	        form.save()
	        messages.success(request, f'Success, Record Saved Successfully')
	        return redirect(labTestType)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = labTestTypeForm()
        form.fields["id"].initial = gnuhealth_lab_test_type.objects.count()+1
        type = "add"
        return render(request, 'health_lab/labTestType.html', {'type': type, 'form': form})


def editLabTestType(request, id):
    type = "edit"
    editForm = gnuhealth_lab_test_type.objects.get(id=id)
    return render(request, 'health_lab/labTestType.html', {'form': editForm, 'type': type})


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
