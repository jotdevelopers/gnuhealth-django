from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('healthprofs', views.healthprofs, name='healthprofs'),
    path('addHealthProf', views.addHealthProf, name='addHealthProf'),
    path('editHealthProf/<id>/', views.editHealthProf, name='editHealthProf'),
    path('updateHealthProf/<id>/', views.updateHealthProf, name='updateHealthProf'),
    path('deleteHealthProf/<id>/', views.deleteHealthProf, name='deleteHealthProf'),
]