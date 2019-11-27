from django import forms
from health_configuration.models import *
from health_party.models import *


class ethnicityForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_ethnicity
        fields = "__all__"
        
class occupationForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_occupation
        fields = "__all__"
        
class residenceForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_gene_varient
        fields = "__all__"
        
class countryForm(forms.ModelForm):
    class Meta:  
        model = country_country
        fields = "__all__"
        
class procedureForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_procedure
        fields = "__all__"
        
class specialityForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_specialty
        fields = "__all__"
        
class buildingForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_hospital_building
        fields = "__all__"
        
class imagingTestTypeForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_imaging_test_type
        fields = "__all__"

class varientForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_gene_varient
        fields = "__all__"
        
class genesForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_disease_genes
        fields = "__all__"
        
class varientForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_gene_varient
        fields = "__all__"

class pathologyGroupsForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_pathology_group
        fields = "__all__"

class categoriesForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_pathology_category
        fields = "__all__"

class bodyFunctionsForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_body_function
        fields = "__all__"

class bodyStructuresForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_body_structure
        fields = "__all__"

class activityParticipationForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_activity_and_participation
        fields = "__all__"

class environmentalFactorForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_environmental_factor
        fields = "__all__"

class dietBeliefForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_diet_belief
        fields = "__all__"

class dietTherapeuticForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_diet_therapeutic
        fields = "__all__"


class pediatricGrowthChartForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_pediatrics_growth_charts_who
        fields = "__all__"


















        


        
# class phenotypeForm(forms.ModelForm):
#     class Meta:
#         model = gnuhealth_gene_varient_phenotype
#         fields = "__all__"
        
