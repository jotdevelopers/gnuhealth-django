from django.urls import *
from django.conf.urls import url, include


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('operationalSectors', views.operationalSectors, name='operationalSectors'),
    path('addOperationalSector', views.addOperationalSector, name='addOperationalSector'),
    path('editOperationalSector/<id>', views.editOperationalSector, name='editOperationalSector'),
    path('updateOperationalSector/<id>/', views.updateOperationalSector, name='updateOperationalSector'),
    path('deleteOperationalSector/<id>/', views.deleteOperationalSector, name='deleteOperationalSector'),
    
    path('operationalAreas', views.operationalAreas, name='operationalAreas'),
    path('addOperationalArea', views.addOperationalArea, name='addOperationalArea'),
    path('editOperationalArea/<id>', views.editOperationalArea, name='editOperationalArea'),
    path('updateOperationalArea/<id>/', views.updateOperationalArea, name='updateOperationalArea'),
    path('deleteOperationalArea/<id>/', views.deleteOperationalArea, name='deleteOperationalArea'),
    path('searchOperationalArea/<search_text>/', views.searchOperationalArea, name='searchOperationalArea'),

    
]