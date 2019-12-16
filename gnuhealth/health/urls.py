from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('patients', views.patients, name='patients'),
    path('addPatient/', views.addPatient, name='addPatient'),
    path('updatePatient/<id>/', views.updatePatient, name='updatePatient'),
    path('editPatient/<id>/', views.editPatient, name='editPatient'),
    path('deletePatient/<id>/', views.deletePatient, name='deletePatient'),
    
    path('pols', views.pols, name='pols'),
    path('addPol', views.addPol, name='addPol'),
    path('editPol/<id>/', views.editPol, name='editPol'),
    path('updatePol/<id>/', views.updatePol, name='updatePol'),
    path('deletePol/<id>/', views.deletePol, name='deletePol'),

    path('searchPerson/<search_text>/', views.searchPerson, name='searchPerson'),
    path('searchInstitution/<search_text>/', views.searchInstitution, name='searchInstitution'),
    path('searchCondition/<search_text>/', views.searchCondition, name='searchCondition'),
    path('searchProcedure/<search_text>/', views.searchProcedure, name='searchProcedure'),

]