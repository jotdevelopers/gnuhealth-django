from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'health_genetics/index.html')
 
def addgenetics(request):
    return render(request,'health_genetics/add-person-genetic-info.html')
