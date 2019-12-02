from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appointments', views.appointments, name='appointments'),
    path('addAppointment', views.addAppointment, name='addAppointment'),
]