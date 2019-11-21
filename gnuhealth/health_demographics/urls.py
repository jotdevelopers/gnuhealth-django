from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('birthCertificates', views.birthCertificates, name='birthCertificates'),
    #path('addBirthCertificate', views.addBirthCertificate, name='addBirthCertificate'),
    #path('editBirthCertificate/<id>', views.editBirthCertificate, name='editBirthCertificate'),
    #path('updateBirthCertificate/<id>/', views.updateBirthCertificate, name='updateBirthCertificate'),
    #path('deleteBirthCertificate/<id>/', views.deleteBirthCertificate, name='deleteBirthCertificate'),
    
    path('', views.index, name='index'),
    #path('deathCertificates', views.deathCertificates, name='deathCertificates'),
    #path('addDeathCertificate', views.addDeathCertificate, name='addDeathCertificate'),
    #path('editDeathCertificate/<id>', views.editDeathCertificate, name='editDeathCertificate'),
    #path('updateDeathCertificate/<id>/', views.updateDeathCertificate, name='updateDeathCertificate'),
    #path('deleteDeathCertificate/<id>/', views.deleteDeathCertificate, name='deleteDeathCertificate'),
]