from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addAppointment', views.addAppointment, name='addAppointment'),
]