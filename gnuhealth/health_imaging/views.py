from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_imaging.models import *
from health_party.models import *
from health_imaging.forms import *
from health_configuration.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


def imagingRequests(request):
    type = "grid"
    requests = gnuhealth_imaging_test_request.objects.all()
    return render(request, 'health_imaging/imaging_requests.html'
                  , {'requests': requests
                      , 'type': type})


def addImagingRequest(request):
    if request.method == "POST":
        form = imagingRequestForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_imaging_test_request.objects.latest('id')
        form.fields["id"].initial = latest.id + 1

        id = request.POST['id']
        create_date = request.POST['create_date']
        write_date = request.POST['write_date']
        create_uid = request.POST['create_uid']
        write_uid = request.POST['write_uid']
        comment = request.POST['comment']
        date = request.POST['date']
        doctor = 1
        req = request.POST['request']
        urgent = True
        requested_test = request.POST['requested_test']
        patient = request.POST['patient']
        state = request.POST['state']

        req = gnuhealth_imaging_test_request(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid,
                              comment = comment,

        date = date,
        doctor = doctor,
        request = req,
        urgent = urgent,
        requested_test = requested_test,
        patient = patient,
        state=state)
        req.save()
        
        requests = gnuhealth_imaging_test_request.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_imaging/imaging_requests.html'
                              , {'type': type, 'msg': msg, 'requests': requests})
           # except:
            #    pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = imagingRequestForm()
        latest = gnuhealth_imaging_test_request.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_imaging/imaging_requests.html', {'type': type, 'form': form})


def editImagingRequest(request, id):
    type = "edit"
    editForm = gnuhealth_imaging_test_request.objects.get(id=id)
    return render(request, 'health_imaging/imaging_requests.html', {'form': editForm, 'type': type})


def updateImagingRequest(request, id):
    type = "grid"
    req = gnuhealth_imaging_test_request.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    eth_id = eth.id
    create_date = eth.create_date
    write_date = eth.write_date
    create_uid = eth.create_uid
    write_uid = eth.write_uid
    req = gnuhealth_imaging_test_request(id=eth_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    eth.save()
    msg = "3"
    requests = gnuhealth_imaging_test_request.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_imaging/imaging_requests.html'
                  , {'type': type, 'msg': msg, 'requests': requests})


def deleteImagingRequest(request, id):
    request = gnuhealth_imaging_test_request.objects.get(id=id)
    request.delete()
    type = "grid"
    msg = "2"
    requests = gnuhealth_imaging_test_request.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_imaging/imaging_requests.html'
                  , {'type': type, 'msg': msg, 'requests': requests})


def imagingResults(request):
    type = "grid"
    results = gnuhealth_imaging_test_result.objects.all()
    return render(request, 'health_imaging/imaging_results.html'
                  , {'results': results
                      , 'type': type})


def addImagingResult(request):
    if request.method == "POST":
        form = imagingResultForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        #latest = gnuhealth_imaging_test_result.objects.latest('id')
        form.fields["id"].initial = 1
        id = request.POST['id']
        create_date = request.POST['create_date']
        write_date = request.POST['write_date']
        create_uid = request.POST['create_uid']
        write_uid = request.POST['write_uid']
        comment = request.POST['comment']
        number = request.POST['number']
        date = request.POST['date']
        doctor = 1
        request_date = request.POST['request_date']
        requested_test = 1
        patient = request.POST['patient']

        result = gnuhealth_imaging_test_result(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid,
                              comment = comment,
        number = number,
        date = date,
        doctor = doctor,
        request = 1,
        request_date = request_date,
        requested_test = requested_test,
        patient = patient)
        result.save()
        results = gnuhealth_imaging_test_result.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_imaging/imaging_results.html'
                              , {'type': type, 'msg': msg, 'results': results})
            #except:
             #   pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = imagingResultForm()
        #latest = gnuhealth_imaging_test_result.objects.latest('id')
        form.fields["id"].initial =  1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_imaging/imaging_results.html', {'type': type, 'form': form})


def editImagingResult(request, id):
    type = "edit"
    editForm = gnuhealth_imaging_test_result.objects.get(id=id)
    return render(request, 'health_imaging/imaging_results.html', {'form': editForm, 'type': type})


def updateImagingResult(request, id):
    type = "grid"
    result = gnuhealth_imaging_test_result.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    id = result.id
    create_date = result.create_date
    write_date = result.write_date
    create_uid = result.create_uid
    write_uid = result.write_uid
    result = gnuhealth_ethnicity(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    result.save()
    msg = "3"
    results = gnuhealth_imaging_test_result.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_imaging/imaging_results.html'
                  , {'type': type, 'msg': msg, 'results': results})


def deleteImagingResult(request, id):
    result = gnuhealth_imaging_test_result.objects.get(id=id)
    result.delete()
    type = "grid"
    msg = "2"
    results = gnuhealth_imaging_test_result.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_imaging/imaging_results.html'
                  , {'type': type, 'msg': msg, 'results': results})


def searchPatient(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    patients = gnuhealth_gene_variant.objects.filter(name__startswith=search_text.capitalize())

    if len(patients) == 0:
        patients = gnuhealth_gene_variant.objects.filter(id=search_text)

    return render_to_response('health_imaging/js/ajax-search.html', {'patients': patients})

def searchTest(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    tests = gnuhealth_imaging_test.objects.filter(name__startswith=search_text.capitalize())

    if len(tests) == 0:
        tests = gnuhealth_imaging_test.objects.filter(id=search_text)

    return render_to_response('health_imaging/js/ajax-search.html', {'tests': tests})


def searchDoctor(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    doctors = gnuhealth_healthprofessionals.objects.filter(name__startswith=search_text.capitalize())

    if len(doctors) == 0:
        doctors = gnuhealth_healthprofessionals.objects.filter(id=search_text)

    return render_to_response('health_imaging/js/ajax-search.html', {'doctors': doctors})

def mainImagingTestTypes(request):
    type = "grid"
    test_types = gnuhealth_imaging_test_type.objects.all()
    return render(request, 'health_dx_imaging/imaging_test_types.html', {'test_types': test_types, 'type': type, 'selected': 'DX Imaging Test Types'})


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
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(mainAddImagingTestType)
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
        return render(request, 'health_dx_imaging/imaging_test_types.html', {'type': type, 'form': form, 'selected': 'DX Imaging Test Types'})


def mainEditImagingTestType(request, id):
    type = "edit"
    editForm = gnuhealth_imaging_test_type.objects.get(id=id)
    return render(request, 'health_dx_imaging/imaging_test_types.html', {'form': editForm, 'type': type, 'selected': 'DX Imaging Test Types'})


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
                  {'mainImagingTest': mainImagingTest, 'type': type, 'selected': 'DX Imaging Tests'})


def mainAddImagingTest(request):
    if request.method == "POST":
        form = mainImagingTestForm(request.POST)
        if form.is_valid():
            type = "grid"
            form.save()
            messages.success(request, f'Success, Record Saved Successfully')
            return redirect(mainImagingTest)
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(mainAddImagingTest)
    else:
        form = mainImagingTestForm()
        form.fields["id"].initial = gnuhealth_imaging_test.objects.count()+1
        type = "add"
        return render(request, 'health_dx_imaging/imaging_tests.html', {'type': type, 'form': form, 'selected': 'DX Imaging Tests'})


def mainEditImagingTest(request, id):
    type = "edit"
    editForm = gnuhealth_imaging_test.objects.get(id=id)
    return render(request, 'health_dx_imaging/imaging_tests.html', {'form': editForm, 'type': type, 'selected': 'DX Imaging Tests'})


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
