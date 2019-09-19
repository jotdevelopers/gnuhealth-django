from django.shortcuts import render
from django.http import HttpResponse
from health_genetics.models import gnuhealth_patient_genetic_risk
from health_genetics.forms import HealthGeneticsForm

# Create your views here.

def index(request):
    genetics = gnuhealth_patient_genetic_risk.objects.all()
    return render(request, 'health_genetics/index.html' , {'genetics':genetics})
 
def addgenetics(request):
    if request.method == "POST":  
        form = HealthGeneticsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponse("Data Saved.")  
            except:  
                pass
        else:
            return HttpResponse("Invalid Form.")        
    else:  
        form = HealthGeneticsForm()  
    return render(request,'health_genetics/add-person-genetic-info.html'  ,{'form':form})
