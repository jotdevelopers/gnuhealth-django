from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from health_configuration.models import *
from health_configuration.forms import *


# Create your views here.


def mainImagingTestTypes(request):
    type = "grid"
    test_types = gnuhealth_imaging_test_type.objects.all()
    return render(request, 'health_dx_imaging/imaging_test_types.html', {'test_types': test_types, 'type': type})


def mainAddImagingTestType(request):
    if request.method == "POST":
        form = imagingTestTypeForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                latest = gnuhealth_imaging_test_type.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                test_types = gnuhealth_imaging_test_type.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect(mainImagingTestTypes)
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = imagingTestTypeForm()
        latest = gnuhealth_imaging_test_type.objects.latest('id')
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
        return render(request, 'health_dx_imaging/imaging_test_types.html', {'type': type, 'form': form})


def mainEditImagingTestType(request, id):
    type = "edit"
    editForm = gnuhealth_imaging_test_type.objects.get(id=id)
    return render(request, 'health_dx_imaging/imaging_test_types.html', {'form': editForm, 'type': type})


def mainUpdateImagingTestType(request, id):
    type = "grid"
    eth = gnuhealth_imaging_test_type.objects.get(id=id)
    name = request.POST['name']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    eth = gnuhealth_imaging_test_type(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                                      , write_uid=write_uid, name=name, code=code)
    eth.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')
    
    return redirect(mainImagingTestTypes)
    


def mainDeleteImagingTestType(request, id):
    test = gnuhealth_imaging_test_type.objects.get(id=id)
    test.delete()
    type = "grid"
    test_types = gnuhealth_imaging_test_type.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(mainImagingTestTypes)


def mainImagingTest(request):
    type = "grid"
    mainImagingTest = gnuhealth_imaging_test.objects.all()
    return render(request, 'health_dx_imaging/imaging_tests.html',
                  {'mainImagingTest': mainImagingTest, 'type': type})


def mainAddImagingTest(request):
    if request.method == "POST":
        form = mainImagingTestForm(request.POST)
        if form.is_valid():
            type = "grid"
            form.save()
            messages.success(request, f'Success, Record Saved Successfully')
            return redirect(mainImagingTest)
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = mainImagingTestForm()
        form.fields["id"].initial = gnuhealth_imaging_test.objects.count()+1
        type = "add"
        return render(request, 'health_dx_imaging/imaging_tests.html', {'type': type, 'form': form})


def mainEditImagingTest(request, id):
    type = "edit"
    editForm = gnuhealth_imaging_test.objects.get(id=id)
    return render(request, 'health_dx_imaging/imaging_tests.html', {'form': editForm, 'type': type})


def mainUpdateImagingTest(request, id):
    type = "grid"
    temp = gnuhealth_imaging_test.objects.get(id=id)
    ltt_id = temp.id
    active = request.POST['active']
    code = request.POST['code']
    name = request.POST['name']
    product = request.POST['product']
    test_type = request.POST['test_type']
    create_date = temp.create_date
    write_date = temp.write_date
    create_uid = temp.create_uid
    write_uid = temp.write_uid
    temp = gnuhealth_imaging_test(id=ltt_id, create_date=create_date, write_date=write_date,
                                                create_uid=create_uid, write_uid=write_uid, name=name,
                                                code=code, active=active, product_id=product_id, test_type=test_type)
    temp.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(mainImagingTest)


def mainDeleteImagingTest(request, id):
    temp = gnuhealth_imaging_test.objects.get(id=id)
    temp.delete()
    type = "grid"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(mainImagingTest)
