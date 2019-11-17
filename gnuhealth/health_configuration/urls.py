from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('condition', views.condition, name='condition'),
    path('ethnicity', views.ethnicity, name='ethnicity'),
    path('addEthnicity', views.addEthnicity, name='addEthnicity'),
    path('editEthnicity/<id>/', views.editEthnicity, name='editEthnicity'),
    path('updateEthnicity/<id>/', views.updateEthnicity, name='updateEthnicity'),
    path('deleteEthnicity/<id>/', views.deleteEthnicity, name='deleteEthnicity'),
    path('citienship', views.citizenship, name='citienship'),
    path('add_citienship', views.add_citizenship, name='add_citienship'),
    path('occupation', views.occupation, name='occupation'),
    path('addOccupation', views.addOccupation, name='addOccupation'),
    path('editOccupation/<id>/', views.editOccupation, name='editOccupation'),
    path('updateOccupation/<id>/', views.updateOccupation, name='updateOccupation'),
    path('deleteOccupation/<id>/', views.deleteOccupation, name='deleteOccupation'),
    path('residence', views.residence, name='residence'),
    path('add_residence', views.add_residence, name='add_residence'),

    path('genes', views.genes, name='genes'),
    path('addGenes', views.addGenes, name='addGenes'),
    path('editGenes/<id>', views.editGenes, name='editGenes'),
    path('updateGenes/<id>/', views.updateGenes, name='updateGenes'),
    path('deleteGenes/<id>/', views.deleteGenes, name='deleteGenes'),
    
    path('varients', views.varients, name='varients'),
    path('addVarient', views.addVarient, name='addVarient'),
    path('editVarient/<id>', views.editVarient, name='editVarient'),
    path('updateVarient/<id>/', views.updateVarient, name='updateVarient'),
    path('deleteVarient/<id>/', views.deleteVarient, name='deleteVarient'),

    path('pathologyGroups', views.pathologyGroups, name='pathologyGroups'),
    path('addPathologyGroups', views.addPathologyGroups, name='addPathologyGroups'),
    path('editPathologyGroups/<id>/', views.editPathologyGroups, name='editPathologyGroups'),
    path('updatePathologyGroups/<id>/', views.updatePathologyGroups, name='updatePathologyGroups'),
    path('deletePathologyGroups/<id>/', views.deletePathologyGroups, name='deletePathologyGroups'),

    path('categories', views.categories, name='categories'),
    path('addCategories', views.addCategories, name='addCategories'),
    path('editCategories/<id>/', views.editCategories, name='editCategories'),
    path('updateCategories/<id>/', views.updateCategories, name='updateCategories'),
    path('deleteCategories/<id>/', views.deleteCategories, name='deleteCategories'),

    path('bodyFunctions', views.bodyFunctions, name='bodyFunctions'),
    path('addBodyFunctions', views.addBodyFunctions, name='addBodyFunctions'),
    path('editBodyFunctions/<id>/', views.editBodyFunctions, name='editBodyFunctions'),
    path('updateBodyFunctions/<id>/', views.updateBodyFunctions, name='updateBodyFunctions'),
    path('deleteBodyFunctions/<id>/', views.deleteBodyFunctions, name='deleteBodyFunctions'),

    path('bodyStructures', views.bodyStructures, name='bodyStructures'),
    path('addBodyStructures', views.addBodyStructures, name='addBodyStructures'),
    path('editBodyStructures/<id>/', views.editBodyStructures, name='editBodyStructures'),
    path('updateBodyStructures/<id>/', views.updateBodyStructures, name='updateBodyStructures'),
    path('deleteBodyStructures/<id>/', views.deleteBodyStructures, name='deleteBodyStructures'),

    path('activityParticipation', views.activityParticipation, name='activityParticipation'),
    path('addActivityParticipation', views.addActivityParticipation, name='addActivityParticipation'),
    path('editActivityParticipation/<id>/', views.editActivityParticipation, name='editActivityParticipation'),
    path('updateActivityParticipation/<id>/', views.updateActivityParticipation, name='updateActivityParticipation'),
    path('deleteActivityParticipation/<id>/', views.deleteActivityParticipation, name='deleteActivityParticipation'),

    path('environmentalFactor', views.environmentalFactor, name='environmentalFactor'),
    path('addEnvironmentalFactor', views.addEnvironmentalFactor, name='addEnvironmentalFactor'),
    path('editEnvironmentalFactor/<id>/', views.editEnvironmentalFactor, name='editEnvironmentalFactor'),
    path('updateEnvironmentalFactor/<id>/', views.updateEnvironmentalFactor, name='updateEnvironmentalFactor'),
    path('deleteEnvironmentalFactor/<id>/', views.deleteEnvironmentalFactor, name='deleteEnvironmentalFactor'),

    path('dietBelief', views.dietBelief, name='dietBelief'),
    path('addDietBelief', views.addDietBelief, name='addDietBelief'),
    path('editDietBelief/<id>/', views.editDietBelief, name='editDietBelief'),
    path('updateDietBelief/<id>/', views.updateDietBelief, name='updateDietBelief'),
    path('deleteDietBelief/<id>/', views.deleteDietBelief, name='deleteDietBelief'),

    path('dietTherapeutic', views.dietTherapeutic, name='dietTherapeutic'),
    path('addDietTherapeutic', views.addDietTherapeutic, name='addDietTherapeutic'),
    path('editDietTherapeutic/<id>/', views.editDietTherapeutic, name='editDietTherapeutic'),
    path('updateDietTherapeutic/<id>/', views.updateDietTherapeutic, name='updateDietTherapeutic'),
    path('deleteDietTherapeutic/<id>/', views.deleteDietTherapeutic, name='deleteDietTherapeutic'),

    path('pediatricsGrowthChart', views.pediatricsGrowthChart, name='pediatricsGrowthChart'),
    path('addPediatricsGrowthChart', views.addPediatricsGrowthChart, name='addPediatricsGrowthChart'),
    path('editPediatricsGrowthChart/<id>/', views.editPediatricsGrowthChart, name='editPediatricsGrowthChart'),
    path('updatePediatricsGrowthChart/<id>/', views.updatePediatricsGrowthChart, name='updatePediatricsGrowthChart'),
    path('deletePediatricsGrowthChart/<id>/', views.deletePediatricsGrowthChart, name='deletePediatricsGrowthChart'),
]