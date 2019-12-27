
from health.models import *  
from health.forms import *
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


# Create your views here.

#Pages of life module

def index(request):
    pols = gnuhealth_pol.objects.all()
    return render(request, 'health/party.html'  , {'pols':pols})
    
def pols(request):
    type = "grid"
    pols = gnuhealth_pol.objects.all()
    return render(request, 'health/pols.html'
                  , {'pols': pols
                      , 'type': type})
    
def patients(request):
    type = "grid"
    patients = gnuhealth_patient.objects.all()
    return render(request, 'health/patients.html'
                  , {'patients': patients
                      , 'type': type})


def addPatient(request):
    if request.method == "POST":
        form = patientForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_patient.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        id = request.POST['id']
        active = True
        biological_sex = None
        blood_type = request.POST['blood_type']
        create_date = request.POST['create_date']
        create_uid = request.POST['create_uid']
        critical_info = request.POST['critical_info']
        current_address = None
        current_insurance = None
        family = request.POST['family']
        general_info = request.POST['general_info']
        hb = request.POST['hb']
        name = request.POST['name']
        primary_care_doctor = None
        rh = None
        domestic_violence = False
        drug_addiction = False
        hostile_area = False
        hours_outside = None
        prison_current = False
        prison_past =False
        relative_in_prison = False
        school_withdrawal = False
        ses_notes = None
        sexual_abuse = False
        single_parent = False
        teenage_pregnancy = False
        working_children = False
        works_at_home = False
        breast_self_examination = False
        write_date = request.POST['write_date']
        write_uid = request.POST['write_uid']
        colposcopy = False
        colposcopy_last = None
        fertile = True
        full_term = None
        mammography = False
        mammography_last = None
        menarche = request.POST['menarche']
        menopausal = False
        menopause = request.POST['menopause']
        pap_test = False
        pap_test_last = None
        age_quit_drinking = None
        age_quit_drugs = None
        age_quit_smoking = None
        age_start_drinking = None
        age_start_drugs = None
        age_start_smoking = None
        alcohol = False
        alcohol_beer_number = None
        alcohol_liquor_number = None
        alcohol_wine_number = None
        anticonceptive = None
        car_child_safety = False
        car_revision = False
        car_seat_belt = False
        coffee = False
        coffee_cups = None
        diet = False
        diet_belief = None
        diet_info = None
        drug_iv = False
        drug_usage = False
        eats_alone = False
        ex_alcoholic = False
        ex_drug_addict = False
        ex_smoker = False
        exercise = False
        exercise_minutes_day = None
        first_sexual_encounter = None
        helmet = False
        home_safety = False
        lifestyle_info = None
        motorcycle_rider = False
        number_of_meals = None
        prostitute =  False
        salt = True
        second_hand_smoker = None
        sex_anal = None
        sex_with_prostitutes =  False
        sexual_partners = None
        sexual_partners_number = None
        sexual_practices = None
        sexual_preferences = None
        sexuality_info = None
        sleep_during_daytime =  False
        sleep_hours = None
        smoking =  False
        smoking_number = None
        soft_drinks = True
        traffic_laws = True
        vegetarian_type = None
        amputee =  False
        amputee_since =  False
        disability =  False
        uxo = False
        patient = gnuhealth_patient(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,active = active,
        biological_sex = biological_sex,
        blood_type = blood_type,
        critical_info = critical_info,
        current_address = current_address,
        current_insurance = current_insurance,
        family = family,
        general_info = general_info,
        hb = hb,
        name = name,
        primary_care_doctor = primary_care_doctor,
        rh = rh,
        domestic_violence = domestic_violence,
        drug_addiction = drug_addiction,
        hostile_area = hostile_area,
        hours_outside = hours_outside,
        prison_current = prison_current,
        prison_past = prison_past,
        relative_in_prison = relative_in_prison,
        school_withdrawal = school_withdrawal,
        ses_notes = ses_notes,
        sexual_abuse = sexual_abuse,
        single_parent = single_parent,
        teenage_pregnancy = teenage_pregnancy,
        working_children = working_children,
        works_at_home = works_at_home,
        breast_self_examination = breast_self_examination,
        colposcopy = colposcopy,
        colposcopy_last = colposcopy_last,
        fertile = fertile,
        full_term = full_term,
        mammography = mammography,
        mammography_last = mammography_last,
        menarche = menarche,
        menopausal = menopausal,
        menopause = menopause,
        pap_test = pap_test,
        pap_test_last = pap_test_last,
        age_quit_drinking = age_quit_drinking,
        age_quit_drugs = age_quit_drugs,
        age_quit_smoking = age_quit_smoking,
        age_start_drinking = age_start_drinking,
        age_start_drugs = age_start_drugs,
        age_start_smoking = age_start_smoking,
        alcohol = alcohol,
        alcohol_beer_number = alcohol_beer_number,
        alcohol_liquor_number = alcohol_liquor_number,
        alcohol_wine_number = alcohol_wine_number,
        anticonceptive = anticonceptive,
        car_child_safety = car_child_safety,
        car_revision = car_revision,
        car_seat_belt = car_seat_belt,
        coffee = coffee,
        coffee_cups = coffee_cups,
        diet = diet,
        diet_belief = diet_belief,
        diet_info = diet_info,
        drug_iv = drug_iv,
        drug_usage = drug_usage,
        eats_alone = eats_alone,
        ex_alcoholic = ex_alcoholic,
        ex_drug_addict = ex_drug_addict,
        ex_smoker = ex_smoker,
        exercise = exercise,
        exercise_minutes_day = exercise_minutes_day,
        first_sexual_encounter = first_sexual_encounter,
        helmet = helmet,
        home_safety = home_safety,
        lifestyle_info = lifestyle_info,
        motorcycle_rider = motorcycle_rider,
        number_of_meals = number_of_meals,
        prostitute =  prostitute,
        salt = salt,
        second_hand_smoker = second_hand_smoker,
        sex_anal = sex_anal,
        sex_with_prostitutes =  sex_with_prostitutes,
        sexual_partners = sexual_partners,
        sexual_partners_number = sexual_partners_number,
        sexual_practices = sexual_practices,
        sexual_preferences = sexual_preferences,
        sexuality_info = sexuality_info,
        sleep_during_daytime =  sleep_during_daytime,
        sleep_hours = sleep_hours,
        smoking =  smoking,
        smoking_number = smoking_number,
        soft_drinks = soft_drinks,
        traffic_laws = traffic_laws,
        vegetarian_type = vegetarian_type,
        amputee =  amputee,
        amputee_since =  amputee_since,
        disability =  disability,
        uxo = uxo)
        patient.save()
        patients = gnuhealth_pol.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health/patients.html'
                              , {'type': type, 'msg': msg, 'patients': patients})
            #except:
             #   pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = patientForm()
        latest = gnuhealth_patient.objects.latest('id')
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
        return render(request, 'health/patients.html', {'type': type, 'form': form})


def editPatient(request, id):
    type = "edit"
    editForm = gnuhealth_patient.objects.get(id=id)
    return render(request, 'health/patients.html', {'form': editForm, 'type': type})


def updatePatient(request, id):
    type = "grid"
    patient = gnuhealth_patient.objects.get(id=id)
    id = patient.id
    age = request.POST['age']
    author = request.POST['author']
    create_date = patient.create_date
    create_uid = patient.create_uid
    federation_account = request.POST['federation_account']
    gene = 1
    health_condition = request.POST['health_condition']
    health_condition_code = request.POST['health_condition_code']
    health_condition_text = None
    info = None
    institution = request.POST['institution']
    medical_context = None
    natural_variant = 1
    node = request.POST['node']
    page = request.POST['page']
    page_date = request.POST['page_date']
    page_type = request.POST['page_type']
    person = request.POST['person']
    phenotype = 1
    procedure = request.POST['procedure']
    procedure_code = request.POST['procedure_code']
    procedure_text = None
    relevance = request.POST['relevance']
    social_context = None
    summary = request.POST['summary']
    write_date = patient.write_date
    write_uid = patient.write_uid
    fsync = True

    patient = gnuhealth_patient(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,age = age,
        author = author,
        federation_account =federation_account,
        gene = gene,
        health_condition = health_condition,
        health_condition_code = health_condition_code,
        health_condition_text = health_condition_text,
        info = info,
        institution = institution,
        medical_context = medical_context,
        natural_variant = natural_variant,
        node = node,
        page = page,
        page_date = page_date,
        page_type = page_type,
        person = person,
        phenotype = phenotype,
        procedure = procedure,
        procedure_code = procedure_code,
        procedure_text = procedure_text,
        relevance = relevance,
        social_context = social_context,
        summary = summary,
        fsync = fsync)
    patient.save()
    
    msg = "3"
    patients = gnuhealth_pol.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health/patients.html'
                  , {'type': type, 'msg': msg, 'patients': patients})


def deletePatient(request, id):
    patient = gnuhealth_patient.objects.get(id=id)
    patient.delete()
    type = "grid"
    msg = "2"
    patients = gnuhealth_patient.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health/patients.html'
                  , {'type': type, 'msg': msg, 'patients': patients})




def addPol(request):
    if request.method == "POST":
        form = polForm(request.POST)
        #if form.is_valid():
         #   try:
        type = "grid"
        msg = "1"
        latest = gnuhealth_pol.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        id = request.POST['id']
        age = request.POST['age']
        author = 1
        create_date = request.POST['create_date']
        create_uid = request.POST['create_uid']
        federation_account = request.POST['federation_account']
        gene = 1
        health_condition = request.POST['health_condition']
        health_condition_code = request.POST['health_condition_code']
        health_condition_text = None
        info = None
        institution = request.POST['institution']
        medical_context = None
        natural_variant = 1
        node = 1
        page = request.POST['page']
        page_date = request.POST['page_date']
        page_type = request.POST['page_type']
        person = request.POST['person']
        phenotype = 1
        procedure = request.POST['procedure']
        procedure_code = request.POST['procedure_code']
        procedure_text = None
        relevance = request.POST['relevance']
        social_context = None
        summary = request.POST['summary']
        write_date = request.POST['write_date']
        write_uid = request.POST['write_uid']
        fsync = True

        pol = gnuhealth_pol(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,age = age,
        author = author,
        federation_account =federation_account,
        gene = gene,
        health_condition = health_condition,
        health_condition_code = health_condition_code,
        health_condition_text = health_condition_text,
        info = info,
        institution = institution,
        medical_context = medical_context,
        natural_variant = natural_variant,
        node = node,
        page = page,
        page_date = page_date,
        page_type = page_type,
        person = person,
        phenotype = phenotype,
        procedure = procedure,
        procedure_code = procedure_code,
        procedure_text = procedure_text,
        relevance = relevance,
        social_context = social_context,
        summary = summary,
        fsync = fsync)
        pol.save()
        pols = gnuhealth_pol.objects.all()
        messages.success(request, f'Success, Record Saved Successfully')
        return render(request, 'health/pols.html'
                              , {'type': type, 'msg': msg, 'pols': pols})
            #except:
             #   pass
        #else:
         #   messages.error(request, f'Sorry, Record Save Error')
          #  return HttpResponse("Invalid Form.")
    else:
        form = polForm()
        latest = gnuhealth_pol.objects.latest('id')
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
        return render(request, 'health/pols.html', {'type': type, 'form': form})


def editPol(request, id):
    type = "edit"
    editForm = gnuhealth_pol.objects.get(id=id)
    return render(request, 'health/pols.html', {'form': editForm, 'type': type})


def updatePol(request, id):
    type = "grid"
    pol = gnuhealth_pol.objects.get(id=id)
    id = pol.id
    age = request.POST['age']
    author = 1
    create_date = request.POST['create_date']
    create_uid = pol.create_uid
    federation_account = request.POST['federation_account']
    gene = 1
    health_condition = request.POST['health_condition']
    health_condition_code = request.POST['health_condition_code']
    health_condition_text = None
    info = None
    institution = request.POST['institution']
    medical_context = None
    natural_variant = 1
    node = 1
    page = request.POST['page']
    page_date = request.POST['page_date']
    page_type = request.POST['page_type']
    person = request.POST['person']
    phenotype = 1
    procedure = request.POST['procedure']
    procedure_code = request.POST['procedure_code']
    procedure_text = None
    relevance = request.POST['relevance']
    social_context = None
    summary = request.POST['summary']
    write_date = request.POST['write_date']
    write_uid = pol.write_uid
    fsync = True

    pol = gnuhealth_pol(id=id, write_date=write_date, write_uid=write_uid,create_date=create_date,
        create_uid=create_uid,age = age,
        author = author,
        federation_account =federation_account,
        gene = gene,
        health_condition = health_condition,
        health_condition_code = health_condition_code,
        health_condition_text = health_condition_text,
        info = info,
        institution = institution,
        medical_context = medical_context,
        natural_variant = natural_variant,
        node = node,
        page = page,
        page_date = page_date,
        page_type = page_type,
        person = person,
        phenotype = phenotype,
        procedure = procedure,
        procedure_code = procedure_code,
        procedure_text = procedure_text,
        relevance = relevance,
        social_context = social_context,
        summary = summary,
        fsync = fsync)
    pol.save()
    
    msg = "3"
    pols = gnuhealth_pol.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return render(request, 'health/pols.html'
                  , {'type': type, 'msg': msg, 'pols': pols})


def deletePol(request, id):
    pol = gnuhealth_pol.objects.get(id=id)
    pol.delete()
    type = "grid"
    msg = "2"
    pols = gnuhealth_pol.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health/pols.html'
                  , {'type': type, 'msg': msg, 'pols': pols})



def searchPerson(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    person = party_party.objects.filter(name__startswith=search_text.capitalize())

    if len(person) == 0:
        person = party_party.objects.filter(id=search_text)

    return render_to_response('health/js/ajax-search.html', {'person': person})

def searchInstitution(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    institution = gnuhealth_institution.objects.filter(name__startswith=search_text.capitalize())

    if len(institution) == 0:
        institution = gnuhealth_institution.objects.filter(id=search_text)

    return render_to_response('health/js/ajax-search.html', {'institution': institution})

def searchCondition(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    condition = gnuhealth_pathology.objects.filter(name__startswith=search_text.capitalize())

    if len(condition) == 0:
        condition = gnuhealth_pathology.objects.filter(id=search_text)

    return render_to_response('health/js/ajax-search.html', {'condition': condition})

def searchProcedure(request, search_text):
    if request.method == "POST":
        search_text = search_text
    else:
        search_text = ''

    procedure = gnuhealth_procedure.objects.filter(name__startswith=search_text.capitalize())

    if len(procedure) == 0:
        procedure = gnuhealth_procedure.objects.filter(id=search_text)

    return render_to_response('health/js/ajax-search.html', {'procedure': procedure})

