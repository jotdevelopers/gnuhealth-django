from django.shortcuts import render
from django.http import HttpResponse
from health.models import gnuhealth_pol  
from health.forms import PolForm

# Create your views here.

#Pages of life module

def index(request):
    pols = gnuhealth_pol.objects.all()
    return render(request, 'health/party.html'  , {'pols':pols})
      
def addPol(request):
    if request.method == "POST":  
        form = PolForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponse("Data Saved.")  
            except:  
                pass
        else:
            return HttpResponse("Invalid Form.")        
    else:  
        form = PolForm()  
    return render(request, 'health/add_pol.html' ,{'form':form})


def addParty(request):
    if request.method == "POST":
        form = procedureForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_procedure.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                procedures = gnuhealth_procedure.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health/party.html'
                              , {'type': type, 'msg': msg, 'procedures': procedures})
            except:
                pass
        else:
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
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
        return render(request, 'health/party.html', {'type': type, 'form': form})


def test():
    return 

