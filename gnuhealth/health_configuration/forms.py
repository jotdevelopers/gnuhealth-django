from django import forms
from health_configuration.models import *

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
        
class phenotypeForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_gene_varient_phenotype
        fields = "__all__"
        
