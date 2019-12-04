from django.urls import path

from . import views

urlpatterns = [
    path('mainProcedures', views.mainProcedures, name='mainProcedures'),
    path('mainAddProcedure', views.mainAddProcedure, name='mainAddProcedure'),
    path('mainEditProcedure/<id>', views.mainEditProcedure, name='mainEditProcedure'),
    path('mainUpdateProcedure/<id>/', views.mainUpdateProcedure, name='mainUpdateProcedure'),
    path('mainDeleteProcedure/<id>/', views.mainDeleteProcedure, name='mainDeleteProcedure'),
]