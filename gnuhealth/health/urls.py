from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pols', views.pols, name='pols'),
    path('addPol', views.addPol, name='addPol'),




]