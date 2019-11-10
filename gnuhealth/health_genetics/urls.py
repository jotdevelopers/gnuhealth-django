from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addgenetics', views.addgenetics, name='addgenetics'),

    # Genetics module urls start
    
    path('disease_genes/', views.disease_genes, name = "disease_genes"),
    path('natural_variants/', views.natural_variants, name = "natural_variants"),
    path('protein_related_diseases/', views.protein_related_diseases, name = "protein_related_diseases"),
    path('variants_phenotype/', views.variants_phenotype, name = "variants_phenotype"),
	
	# Genetics urls end

]