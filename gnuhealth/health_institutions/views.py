from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from health.models import gnuhealth_pathology
from health_institutions.models import *
from health_party.models import *
from health_institutions.forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")


def institutions(request):
    type = "grid"
    institutions = gnuhealth_institution.objects.all()
    return render(request, 'health_institutions/institutions.html'
                  , {'institutions': institutions
                      , 'type': type})


def addInstitution(request):
    if request.method == "POST":
        form = institutionForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_institution.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        id = request.POST['id']
        beds = request.POST['beds']
        code = request.POST['code']
        extra_info = request.POST['extra_info']
        heliport = True
        institution_type = request.POST['institution_type']
        name = request.POST['name']
        operating_room = True
        or_number = None
        picture = ''
        public_level = request.POST['public_level']
        teaching = True
        trauma_level = ''
        trauma_center = True
        main_specialty = None
        create_date = request.POST['create_date']
        write_date = request.POST['write_date']
        create_uid = request.POST['create_uid']
        write_uid = request.POST['write_uid']
        institution = gnuhealth_institution(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, beds=beds, code=code, extra_info=extra_info, heliport=heliport, institution_type=institution_type,
                              operating_room=operating_room, or_number=or_number, picture = picture, public_level=public_level,
                              teaching=teaching, trauma_level=trauma_level, trauma_center=trauma_center,
                              main_specialty=main_specialty)
        institution.save()
        institutions = gnuhealth_institution.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health_institutions/institutions.html'
                              , {'type': type, 'msg': msg, 'institutions': institutions})
            #except:
           #     pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = institutionForm()
        latest = gnuhealth_institution.objects.latest('id')
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
        return render(request, 'health_institutions/institutions.html', {'type': type, 'form': form})


def editInstitution(request, id):
    type = "edit"
    editForm = gnuhealth_institution.objects.get(id=id)
    return render(request, 'health_institutions/institutions.html', {'form': editForm, 'type': type})


def updateInstitution(request, id):
    type = "grid"
    institution = gnuhealth_institution.objects.get(id=id)
    id = request.POST['id']
    beds = request.POST['beds']
    code = request.POST['code']
    extra_info = request.POST['extra_info']
    heliport = True
    institution_type = request.POST['institution_type']
    name = request.POST['name']
    operating_room = True
    or_number = None
    picture = ''
    public_level = request.POST['public_level']
    teaching = True
    trauma_level = ''
    trauma_center = True
    main_specialty = None
    create_date = request.POST['create_date']
    write_date = request.POST['write_date']
    create_uid = request.POST['create_uid']
    write_uid = request.POST['write_uid']
    institution = gnuhealth_institution(id=id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, beds=beds, code=code, extra_info=extra_info, heliport=heliport, institution_type=institution_type,
                              operating_room=operating_room, or_number=or_number, picture = picture, public_level=public_level,
                              teaching=teaching, trauma_level=trauma_level, trauma_center=trauma_center,
                              main_specialty=main_specialty)
    institution.save()

    msg = "3"
    institutions = gnuhealth_institution.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health_institutions/institutions.html'
                  , {'type': type, 'msg': msg, 'institutions': institutions})


def deleteInstitution(request, id):
    institution = gnuhealth_institution.objects.get(id=id)
    institution.delete()
    type = "grid"
    msg = "2"
    institutions = gnuhealth_institution.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_institutions/institutions.html'
                  , {'type': type, 'msg': msg, 'institutions': institutions})

def searchInstitution(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    institutions = party_party.objects.filter(name__startswith=search_text.capitalize())

    if len(institutions) == 0:
        institutions = party_party.objects.filter(id=search_text)

    return render_to_response('health_institutions/js/ajax-search.html', {'institutions': institutions})
