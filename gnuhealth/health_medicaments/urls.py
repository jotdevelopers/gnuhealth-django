from django.urls import path

from . import views

urlpatterns = [
    path('medicamentCategory', views.medicamentCategory, name='medicamentCategory'),
    path('addMedicamentCategory', views.addMedicamentCategory, name='addMedicamentCategory'),
    path('editMedicamentCategory/<id>/', views.editMedicamentCategory, name='editMedicamentCategory'),
    path('updateMedicamentCategory/<id>/', views.updateMedicamentCategory, name='updateMedicamentCategory'),
    path('deleteMedicamentCategory/<id>/', views.deleteMedicamentCategory, name='deleteMedicamentCategory'),

    path('drugForm', views.drugForm, name='drugForm'),
    path('addDrugForm', views.addDrugForm, name='addDrugForm'),
    path('editDrugForm/<id>/', views.editDrugForm, name='editDrugForm'),
    path('updateDrugForm/<id>/', views.updateDrugForm, name='updateDrugForm'),
    path('deleteDrugForm/<id>/', views.deleteDrugForm, name='deleteDrugForm'),

    path('drugRoute', views.drugRoute, name='drugRoute'),
    path('addDrugRoute', views.addDrugRoute, name='addDrugRoute'),
    path('editDrugRoute/<id>/', views.editDrugRoute, name='editDrugRoute'),
    path('updateDrugRoute/<id>/', views.updateDrugRoute, name='updateDrugRoute'),
    path('deleteDrugRoute/<id>/', views.deleteDrugRoute, name='deleteDrugRoute'),

    path('doseUnit', views.doseUnit, name='doseUnit'),
    path('addDoseUnit', views.addDoseUnit, name='addDoseUnit'),
    path('editDoseUnit/<id>/', views.editDoseUnit, name='editDoseUnit'),
    path('updateDoseUnit/<id>/', views.updateDoseUnit, name='updateDoseUnit'),
    path('deleteDoseUnit/<id>/', views.deleteDoseUnit, name='deleteDoseUnit'),

    path('medicationDosage', views.medicationDosage, name='medicationDosage'),
    path('addMedicationDosage', views.addMedicationDosage, name='addMedicationDosage'),
    path('editMedicationDosage/<id>/', views.editMedicationDosage, name='editMedicationDosage'),
    path('updateMedicationDosage/<id>/', views.updateMedicationDosage, name='updateMedicationDosage'),
    path('deleteMedicationDosage/<id>/', views.deleteMedicationDosage, name='deleteMedicationDosage'),

    path('medicament', views.medicament, name='medicament'),
    path('addMedicament', views.addMedicament, name='addMedicament'),
    path('editMedicament/<id>/', views.editMedicament, name='editMedicament'),
    path('updateMedicament/<id>/', views.updateMedicament, name='updateMedicament'),
    path('deleteMedicament/<id>/', views.deleteMedicament, name='deleteMedicament'),
]