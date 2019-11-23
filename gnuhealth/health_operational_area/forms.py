from django import forms
from health_operational_area.models import *

class operationalSectorForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_operational_sector
        fields = "__all__"

class operationalAreaForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_operational_area
        fields = "__all__"

















        


        
# class phenotypeForm(forms.ModelForm):
#     class Meta:
#         model = gnuhealth_gene_varient_phenotype
#         fields = "__all__"
        
