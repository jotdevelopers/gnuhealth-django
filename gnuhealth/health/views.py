from django.shortcuts import render
from django.http import HttpResponse
from health.models import gnuhealth_pol  
from health.forms import HealthpolForm

# Create your views here.

def index(request):
   # pols = gnuhealth_pol.objects.all()
    return render(request, 'health/index.html' ) #, {'pols':pols})
    #return render(request,'index.html')
    #return HttpResponse("Hello, world. 1226363sdsddd22773")

def base(request):
   # pols = gnuhealth_pol.objects.all()
    return render(request, 'health/base.html' )

def addpol(request):
    return render(request, 'health/addpol.html')

def addpolsubmit(request):
    
    person= request.POST["person"]
    age = request.POST["age"]
    node= request.POST["node"]
    account= request.POST["account"]
    
    
    return render(request, 'health/addpol.html')

def test():
    return ;

