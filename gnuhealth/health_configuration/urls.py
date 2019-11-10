from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('condition', views.condition, name='condition'),
    path('pathologyGroups', views.pathologyGroups, name='pathologyGroups'),
    path('ethnicity', views.ethnicity, name='ethnicity'),
    path('add_ethnicity', views.add_ethnicity, name='add_ethnicity'),
    path('citienship', views.citizenship, name='citienship'),
    path('add_citienship', views.add_citizenship, name='add_citienship'),
    path('occupation', views.occupation, name='occupation'),
    path('add_occupation', views.add_occupation, name='add_occupation'),
    path('residence', views.residence, name='residence'),
    path('add_residence', views.add_residence, name='add_residence'),
]