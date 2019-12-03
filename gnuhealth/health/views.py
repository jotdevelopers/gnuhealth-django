
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
    pols = gnuhealth_pol.objects.all()
    return render(request, 'health/patients.html'
                  , {'pols': pols
                      , 'type': type})

def addPol(request):
    if request.method == "POST":
        form = polForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                #latest = gnuhealth_pol.objects.latest('id')
                form.fields["id"].initial =  1
                form.save()
                pols = gnuhealth_pol.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health/pols.html'
                              , {'type': type, 'msg': msg, 'pols': pols})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = polForm()
        #latest = gnuhealth_pol.objects.latest('id')
        #form.fields["id"].initial = latest.id + 1
        form.fields["id"].initial =  1
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


