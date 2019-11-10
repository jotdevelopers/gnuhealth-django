from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_pol', views.add_pol, name='add_pol'),



]