from django.shortcuts import render
from django.http import HttpResponse
from health.models import gnuhealth_pol  
from health.forms import PolForm

# Create your views here.

def index(request):
    pols = gnuhealth_pol.objects.all()
    return render(request, 'health/index.html', {'pols':pols})


def base(request):
    return render(request, 'health/base.html' )
   # pols = gnuhealth_pol.objects.all()
    

def addpol(request):
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
    return render(request, 'health/addpol.html' ,{'form':form})

def addpolsubmit(request):
    if request.method == "POST":  
        form = HealthpolForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/index')  
            except:  
                pass  
    else:  
        form = HealthpolForm()  
    return render(request, 'health/addpol.html')

def test():
    return ;

