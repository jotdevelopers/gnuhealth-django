from django.urls import *
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('condition', views.condition, name='condition'),
    
    #Patient
    path('ethnicity', views.ethnicity, name='ethnicity'),
    path('addEthnicity', views.addEthnicity, name='addEthnicity'),
    path('editEthnicity/<id>/', views.editEthnicity, name='editEthnicity'),
    path('updateEthnicity/<id>/', views.updateEthnicity, name='updateEthnicity'),
    path('deleteEthnicity/<id>/', views.deleteEthnicity, name='deleteEthnicity'),
    
    path('occupation', views.occupation, name='occupation'),
    path('addOccupation', views.addOccupation, name='addOccupation'),
    path('editOccupation/<id>/', views.editOccupation, name='editOccupation'),
    path('updateOccupation/<id>/', views.updateOccupation, name='updateOccupation'),
    path('deleteOccupation/<id>/', views.deleteOccupation, name='deleteOccupation'),
    
    
    path('citienship', views.citizenship, name='citienship'),
    path('add_citienship', views.add_citizenship, name='add_citienship'),

    path('residence', views.residence, name='residence'),
    path('add_residence', views.add_residence, name='add_residence'),
    
    #hospitalization

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

    path('phenotypes', views.phenotypes, name='phenotypes'),
    path('addPhenotype', views.addPhenotype, name='addPhenotype'),
    path('editPhenotype/<id>', views.editPhenotype, name='editPhenotype'),
    path('updatePhenotype/<id>/', views.updatePhenotype, name='updatePhenotype'),
    path('deletePhenotype/<id>/', views.deleteVarient, name='deleteVarient'),

    path('proteins', views.proteins, name='proteins'),
    path('addProtein', views.addProtein, name='addProtein'),
    path('editProtein/<id>', views.editProtein, name='editProtein'),
    path('updateProtein/<id>/', views.updateProtein, name='updateProtein'),
    path('deleteProtein/<id>/', views.deleteProtein, name='deleteProtein'),
    path('searchVarient/<search_text>/', views.searchVarient, name='searchVarient'),
    path('searchPhenotype/<search_text>/', views.searchPhenotype, name='searchPhenotype'),

    #procedure
    path('procedures', views.procedures, name='procedures'),
    path('addProcedure', views.addProcedure, name='addProcedure'),
    #path('editProcedure/<id>', views.editProcedure, name='editProcedure'),
    #path('updateProcedure/<id>/', views.updateProcedure, name='updateProcedure'),
    path('deleteProcedure/<id>/', views.deleteProcedure, name='deleteProcedure'),
    
    #Dx Imaging
    path('imagingTestTypes', views.imagingTestTypes, name='imagingTestTypes'),
    path('addImagingTestType', views.addImagingTestType, name='addImagingTestType'),
    path('editImagingTestType/<id>', views.editImagingTestType, name='editdImagingTestType'),
    path('updateImagingTestType/<id>/', views.updateImagingTestType, name='updateImagingTestType'),
    path('deleteImagingTestType/<id>/', views.deleteImagingTestType, name='deleteImagingTestType'),
    
    #work schedule
    path('specialities', views.specialities, name='specialities'),
    path('addSpeciality', views.addSpeciality, name='addSpeciality'),
    path('editSpeciality/<id>', views.editSpeciality, name='editSpeciality'),
    path('updateSpeciality/<id>/', views.updateSpeciality, name='updateSpeciality'),
    path('deleteSpeciality/<id>/', views.deleteSpeciality, name='deleteSpeciality'),
    
    #institutions
    path('buildings', views.buildings, name='buildings'),
    path('addBuilding', views.addBuilding, name='addBuilding'),
    path('editBuilding/<id>', views.editBuilding, name='editBuilding'),
    path('updateBuilding/<id>/', views.updateBuilding, name='updateBuilding'),
    path('deleteBuilding/<id>/', views.deleteBuilding, name='deleteBuilding'),

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
    
    #demographics
    path('country', views.country, name='country'),
    path('addCountry', views.addCountry, name='addCountry'),
    path('editCountry/<id>/', views.editCountry, name='editCountry'),
    path('updateCountry/<id>/', views.updateCountry, name='updateCountry'),
    path('deleteCountry/<id>/', views.deleteCountry, name='deleteCountry'),

    path('subdivisions', views.subdivisions, name='subdivisions'),
    path('addSubdivision', views.addSubdivision, name='addSubdivision'),
    path('editSubdivision/<id>/', views.editSubdivision, name='editSubdivision'),
    path('updateSubdivision/<id>/', views.updateSubdivision, name='updateSubdivision'),
    path('deleteSubdivision/<id>/', views.deleteSubdivision, name='deleteSubdivision'),
    path('searchCountry/<search_text>/', views.searchCountry, name='searchCountry'),
]

