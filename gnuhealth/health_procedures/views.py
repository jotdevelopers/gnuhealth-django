from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from health_configuration.models import gnuhealth_procedure
from health_configuration.forms import procedureForm


def mainProcedures(request):
    type = "grid"
    procedures = gnuhealth_procedure.objects.order_by('-id')[:1000]
    return render(request, 'health_procedures/procedures.html'
                  , {'procedures': procedures
                      , 'type': type, 'selected': 'Procedures'})


def mainAddProcedure(request):
    if request.method == "POST":
        form = procedureForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_procedure.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                messages.success(request, f'Success, Record Saved Successfully')
                return redirect(mainProcedures)
            except:
                pass
        else:
            messages.warning(request, f'Sorry, Record Save Error - Invalid Fields')
            return redirect(mainAddProcedure)
    else:
        form = procedureForm()
        latest = gnuhealth_procedure.objects.latest('id')
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
        return render(request, 'health_procedures/procedures.html', {'type': type, 'form': form, 'selected': 'Procedures'})


def mainEditProcedure(request, id):
    type = "edit"
    editForm = gnuhealth_procedure.objects.get(id=id)
    return render(request, 'health_procedures/procedures.html', {'form': editForm, 'type': type})


def mainUpdateProcedure(request, id):
    type = "grid"
    procedure = gnuhealth_procedure.objects.get(id=id)
    name = request.POST['name']
    description = request.POST['description']
    pro_id = procedure.id
    create_date = procedure.create_date
    write_date = procedure.write_date
    create_uid = procedure.create_uid
    write_uid = procedure.write_uid
    procedure = gnuhealth_procedure(id=pro_id, create_date=create_date, write_date=write_date,
                                           create_uid=create_uid, write_uid=write_uid, name=name,
                                           description=description)
    procedure.save()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')

    return redirect(mainProcedures)


def mainDeleteProcedure(request, id):
    procedure = gnuhealth_procedure.objects.get(id=id)
    procedure.delete()
    type = "grid"
    msg = "2"
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return redirect(mainProcedures)
