from django.urls import path

from . import views

urlpatterns = [
    # Archives module urls start

    path('archives_main/', views.archives_main, name = "archives_main"),
    path('archives_add/', views.archives_add, name = "archives_add"),
    
	# Archives module urls end
]