from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
   
    path('families', views.families, name='families'),
    path('addFamily', views.addFamily, name='addFamily'),
    path('editFamily/<id>/', views.editFamily, name='editFamily'),
    path('updateFamily/<id>/', views.updateFamily, name='updateFamily'),
    path('deleteFamily/<id>/', views.deleteFamily, name='deleteFamily'),

    path('familyMembers', views.familyMembers, name='familyMembers'),
    path('addFamilyMember', views.addFamilyMember, name='addFamilyMember'),
    path('editFamilyMember/<id>/', views.editFamilyMember, name='editFamilyMember'),
    path('updateFamilyMember/<id>/', views.updateFamilyMember, name='updateFamilyMember'),
    path('deleteFamilyMember/<id>/', views.deleteFamilyMember, name='deleteFamilyMember'),

   
]