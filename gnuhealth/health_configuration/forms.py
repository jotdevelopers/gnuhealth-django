from django import forms
from django.forms import ModelMultipleChoiceField
from health_configuration.models import *
from health_party.models import *
from django_select2.forms import Select2MultipleWidget

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
        model = country_country
        fields = "__all__"
        
class countryForm(forms.ModelForm):
    class Meta:  
        model = country_country
        fields = "__all__"
        
class subdivisionForm(forms.ModelForm):
    class Meta:
        model = country_subdivision
        fields = "__all__"
        country = ModelMultipleChoiceField(queryset=country_country.objects.values_list('name', flat=True), widget=Select2MultipleWidget)

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
        model = gnuhealth_gene_variant
        fields = "__all__"

class phenotypeForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_gene_variant
        fields = "__all__"
        variant = ModelMultipleChoiceField(queryset=gnuhealth_gene_variant_phenotype.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        phenotype = ModelMultipleChoiceField(queryset=gnuhealth_gene_variant_phenotype.objects.values_list('name', flat=True), widget=Select2MultipleWidget)


class proteinForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_protein_disease
        fields = "__all__"    

class genesForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_disease_gene
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


class mainImagingTestForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_imaging_test
        fields = ['id','active','code','name','product','test_type','create_date', 'write_date']
