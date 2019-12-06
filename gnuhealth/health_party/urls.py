from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add Party
    path('party', views.party, name='party'),
    path('addParty', views.addParty, name='addParty'),
    path('editParty/<id>', views.editParty, name='editParty'),
    path('updateParty/<id>/', views.updateParty, name='updateParty'),
    path('searchEthnicity/<search_text>/', views.searchEthnicity, name='searchEthnicity'),
    path('deleteParty/<id>/', views.deleteParty, name='deleteParty'),
    path('searchCitizenship/<search_text>/', views.searchCitizenship, name='searchCitizenship'),
    path('searchEthnicity/<search_text>/', views.searchEthnicity, name='searchEthnicity'),
    path('searchOccupation/<search_text>/', views.searchOccupation, name='searchOccupation'),
    path('searchDU/<search_text>/', views.searchDU, name='searchDU'),
    path('searchResidence/<search_text>/', views.searchResidence, name='searchResidence'),

]