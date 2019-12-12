from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
   
    path('families', views.families, name='families'),
    path('addFamily', views.addFamily, name='addFamily'),
    path('editFamily/<id>/', views.editFamily, name='editFamily'),
    path('updateFamily/<id>/', views.updateFamily, name='updateFamily'),
    path('deleteFamily/<id>/', views.deleteFamily, name='deleteFamily'),

    path('du', views.du, name='du'),
    path('addDu', views.addDu, name='addDu'),
    path('editDu/<id>/', views.editDu, name='editDu'),
    path('updateDu/<id>/', views.updateDu, name='updateDu'),
    path('deleteDu/<id>/', views.deleteDu, name='deleteDu'),

    path('birthCertificates', views.birthCertificates, name='birthCertificates'),
    path('addBirthCertificate', views.addBirthCertificate, name='addBirthCertificate'),
    path('editBirthCertificate/<id>/', views.editBirthCertificate, name='editBirthCertificate'),
    path('updateBirthCertificate/<id>/', views.updateBirthCertificate, name='updateBirthCertificate'),
    path('deleteBirthCertificate/<id>/', views.deleteBirthCertificate, name='deleteBirthCertificate'),

    path('deathCertificates', views.deathCertificates, name='deathCertificates'),
    path('addDeathCertificate', views.addDeathCertificate, name='addDeathCertificate'),
    path('editDeathCertificate/<id>/', views.editDeathCertificate, name='editDeathCertificate'),
    path('updateDeathCertificate/<id>/', views.updateDeathCertificate, name='updateDeathCertificate'),
    path('deleteDeathCertificate/<id>/', views.deleteDeathCertificate, name='deleteDeathCertificate'),

    path('familyMembers', views.familyMembers, name='familyMembers'),
    path('addFamilyMember', views.addFamilyMember, name='addFamilyMember'),
    path('editFamilyMember/<id>/', views.editFamilyMember, name='editFamilyMember'),
    path('updateFamilyMember/<id>/', views.updateFamilyMember, name='updateFamilyMember'),
    path('deleteFamilyMember/<id>/', views.deleteFamilyMember, name='deleteFamilyMember'),
    path('searchCountry/<search_text>/', views.searchCountry, name='searchCountry'),
    path('searchSubdiv/<search_text>/', views.searchSubdiv, name='searchSubdiv'),
    path('searchOpsector/<search_text>/', views.searchOpsector, name='searchOpsector'),

   
]