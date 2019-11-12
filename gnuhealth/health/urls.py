from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addPol', views.addPol, name='addPol'),



]