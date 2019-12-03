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

]