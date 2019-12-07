from django.urls import *
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('immunizationSchedule', views.immunizationSchedule, name='immunizationSchedule'),
    path('addImmunizationSchedule', views.addImmunizationSchedule, name='addImmunizationSchedule'),
    path('editImmunizationSchedule/<id>/', views.editImmunizationSchedule, name='editImmunizationSchedule'),
    path('updateImmunizationSchedule/<id>/', views.updateImmunizationSchedule, name='updateImmunizationSchedule'),
    path('deleteImmunizationSchedule/<id>/', views.deleteImmunizationSchedule, name='deleteImmunizationSchedule'),
    
    path('vaccineDoses', views.vaccineDoses, name='vaccineDoses'),
    path('addVaccineDoses', views.addVaccineDoses, name='addVaccineDoses'),
    path('editVaccineDoses/<id>/', views.editVaccineDoses, name='editVaccineDoses'),
    path('updateVaccineDoses/<id>/', views.updateVaccineDoses, name='updateVaccineDoses'),
    path('deleteVaccineDoses/<id>/', views.deleteVaccineDoses, name='deleteVaccineDoses'),
    
    path('scheduleLine', views.scheduleLine, name='scheduleLine'),
    path('addScheduleLine', views.addScheduleLine, name='addScheduleLine'),
    path('editScheduleLine/<id>/', views.editScheduleLine, name='editScheduleLine'),
    path('updateScheduleLine/<id>/', views.updateScheduleLine, name='updateScheduleLine'),
    path('deleteScheduleLine/<id>/', views.deleteScheduleLine, name='deleteScheduleLine'),
]