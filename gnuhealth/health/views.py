from django.shortcuts import render
from django.http import HttpResponse
from health.models import gnuhealth_pol  
from health.forms import PolForm

# Create your views here.

#Pages of life module

def index(request):
    pols = gnuhealth_pol.objects.all()
    return render(request, 'health/index.html'  , {'pols':pols})
      
def add_pol(request):
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

def test():
    return 

#Dashboard

def sankey(request):
    return render(request, 'health/SANKEY.html'  )

def visits(request):
    return render(request, 'health/visits.html'  )

def sunburst(request):
    return render(request, 'health/sunburst.html'  )

def radar(request):
    return render(request, 'health/radar.html'  )
