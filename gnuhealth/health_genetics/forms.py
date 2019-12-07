from django import forms  
from health_genetics.models import *
from health_configuration.models import *
from django.forms import ModelMultipleChoiceField
from django_select2.forms import Select2MultipleWidget
class geneticForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_patient_genetic_risk   
        fields = "__all__" 
        natural_variant = ModelMultipleChoiceField(queryset=gnuhealth_gene_variant.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
