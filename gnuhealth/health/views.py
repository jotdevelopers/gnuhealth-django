from django.shortcuts import render
from django.http import HttpResponse
from health.models import gnuhealth_pol  

# Create your views here.

def index(request):
    gnuhealth_pols = gnuhealth_pol.objects.all()
    return render(request, 'health/index.html')
    #return render(request,'index.html')
    #return HttpResponse("Hello, world. 1226363sdsddd22773")

def addpol(request):
    return render(request, 'health/addpol.html')

def test():
    return ;

def health(request):  
    if request.method == "POST":  
        form = HealthpolForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_pol')  
            except:  
                pass  
    else:  
        form = HealthpolForm()  
    return render(request,'index.html',{'form':form})  
def show_pol(request):  
    gnuhealth_pols = gnuhealth_pol.objects.all()  
    return render(request,"show_pol.html",{'gnuhealth_pols': gnuhealth_pols})  
def edit_pol(request, id):  
    gnuhealth_pol = gnuhealth_pol.objects.get(id=id)  
    return render(request,'edit_pol.html', {'gnuhealth_pol':gnuhealth_pol})  
def update_pol(request, id):  
    gnuhealth_pol = gnuhealth_pol.objects.get(id=id)  
    form = HealthpolForm(request.POST, instance = gnuhealth_pol)  
    if form.is_valid():  
        form.save()  
        return redirect("/show_pol")  
    return render(request, 'edit_pol.html', {'gnuhealth_pol': gnuhealth_pol})  
def destroy_pol(request, id):  
    gnuhealth_pol = gnuhealth_pol.objects.get(id=id)  
    gnuhealth_pol.delete()  
    return redirect("/show_pol")  