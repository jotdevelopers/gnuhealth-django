from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Federation module urls start

    path('queue_manager_main/', views.queue_manager_main, name = "queue_manager_main"),
	
	# Federation urls end
]