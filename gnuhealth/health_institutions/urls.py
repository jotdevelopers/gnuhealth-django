from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('institutions', views.institutions, name='institutions'),
    path('addInstitution', views.addInstitution, name='addInstitution'),
    path('editInstitution/<id>/', views.editInstitution, name='editInstitution'),
    path('updateInstitution//<id>/', views.updateInstitution, name='updateInstitution'),
    path('deleteInstitution/<id>/', views.deleteInstitution, name='deleteInstitution'),
    path('searchInstitution/<search_text>/', views.searchInstitution, name='searchInstitution'),
]