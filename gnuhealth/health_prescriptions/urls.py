from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prescriptions', views.prescriptions, name='prescriptions'),
    path('addPrescription', views.addPrescription, name='addPrescription'),
    path('editPrescription/<id>', views.editPrescription, name='editPrescription'),
    path('updatePrescription/<id>/', views.updatePrescription, name='updatePrescription'),
    path('deletePrescription/<id>/', views.deletePrescription, name='deletePrescription'),

]