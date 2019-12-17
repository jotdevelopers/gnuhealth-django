from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appointments', views.appointments, name='appointments'),
    path('addAppointment', views.addAppointment, name='addAppointment'),
    path('editAppointment/<id>/', views.editAppointment, name='editAppointment'),
    path('updateAppointment/<id>/', views.updateAppointment, name='updateAppointment'),
    path('deleteAppointment/<id>/', views.deleteAppointment, name='deleteAppointment'),
]