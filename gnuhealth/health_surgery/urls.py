from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('surgeries', views.surgeries, name='surgeries'),
    path('addSurgery', views.addSurgery, name='addSurgery'),
    path('editSurgery/<id>/', views.editSurgery, name='editSurgery'),
    path('updateSurgery/<id>/', views.updateSurgery, name='updateSurgery'),
    path('deleteSurgery/<id>/', views.deleteSurgery, name='deleteSurgery'),
]