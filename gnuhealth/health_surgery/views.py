from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'health_surgery/index.html')

 def addsurgery(request):
     if request.method == "POST":  
        form = HealthSurgeryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/index')  
            except:  
                pass  
    else:  
        form = HealthSurgeryForm()  
    return render(request,'health_surgery/add-surgery.html',{'form':form})
