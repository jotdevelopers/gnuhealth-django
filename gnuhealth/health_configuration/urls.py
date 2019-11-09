from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('condition', views.condition, name='condition'),
    path('pathologyGroups', views.pathologyGroups, name='pathologyGroups'),
]