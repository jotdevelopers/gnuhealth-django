from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'health_surgery/index.html')

def addsurgery(request):
    return render(request,'health_surgery/add-surgery.html')
