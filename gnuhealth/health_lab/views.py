from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'health_lab/index.html')

def addlabtestrequest(request):
    if request.method == "POST":  
        form = HealthLabForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/index')  
            except:  
                pass  
    else:  
        form = HealthLabForm()  
    return render(request,'health_lab/add-lab-test-request.html',{'form':form})  

def labtestresult(request):
    return render(request, 'health_lab/lab-test-results.html')
