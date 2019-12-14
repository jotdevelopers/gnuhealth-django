from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pols', views.pols, name='pols'),
    path('addPol', views.addPol, name='addPol'),
    path('patients', views.patients, name='patients'),
    path('editPol/<id>/', views.editPol, name='editPol'),
    path('updatePol/<id>/', views.updatePol, name='updatePol'),
    path('deletePol/<id>/', views.deletePol, name='deletePol'),
    path('searchPerson/<search_text>/', views.searchPerson, name='searchPerson'),
    path('searchInstitution/<search_text>/', views.searchInstitution, name='searchInstitution'),
    path('searchCondition/<search_text>/', views.searchCondition, name='searchCondition'),
    path('searchProcedure/<search_text>/', views.searchProcedure, name='searchProcedure'),

]