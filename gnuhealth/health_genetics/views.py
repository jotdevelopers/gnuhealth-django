from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'health_genetics/index.html')
 
 def addgenetics(request):
     if request.method == "POST":  
        form = HealthGeneticsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/index')  
            except:  
                pass  
    else:  
        form = HealthGeneticsForm()  
    return render(request,'health/add-person-genetic-info.html',{'form':form})
