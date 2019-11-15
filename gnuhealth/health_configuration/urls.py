from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('condition', views.condition, name='condition'),
    path('pathologyGroups', views.pathologyGroups, name='pathologyGroups'),
    path('ethnicity', views.ethnicity, name='ethnicity'),
    path('addEthnicity', views.addEthnicity, name='addEthnicity'),
    path('editEthnicity/<id>/', views.editEthnicity, name='editEthnicity'),
    path('updateEthnicity/<id>/', views.updateEthnicity, name='updateEthnicity'),
    path('deleteEthnicity/<id>/', views.deleteEthnicity, name='deleteEthnicity'),
    path('citienship', views.citizenship, name='citienship'),
    path('add_citienship', views.add_citizenship, name='add_citienship'),
    path('occupation', views.occupation, name='occupation'),
    path('addOccupation', views.addOccupation, name='addOccupation'),
    path('editOccupation/<id>/', views.editOccupation, name='editOccupation'),
    path('updateOccupation/<id>/', views.updateOccupation, name='updateOccupation'),
    path('deleteOccupation/<id>/', views.deleteOccupation, name='deleteOccupation'),
    path('residence', views.residence, name='residence'),
    path('add_residence', views.add_residence, name='add_residence'),

    path('genes', views.genes, name='genes'),
    path('addGenes', views.addGenes, name='addGenes'),
    path('editGenes/<id>', views.editGenes, name='editGenes'),
    path('updateGenes/<id>/', views.updateGenes, name='updateGenes'),
    path('deleteGenes/<id>/', views.deleteGenes, name='deleteGenes'),
    
    path('varients', views.varients, name='varients'),
    path('addVarient', views.addVarient, name='addVarient'),
    path('editVarient/<id>', views.editVarient, name='editVarient'),
    path('updateVarient/<id>/', views.updateVarient, name='updateVarient'),
    path('deleteVarient/<id>/', views.deleteVarient, name='deleteVarient'),
]