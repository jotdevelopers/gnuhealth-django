from django import forms
from health_operational_area.models import *
from django import forms
from django.forms import ModelMultipleChoiceField
from health_party.models import *
from django_select2.forms import Select2MultipleWidget

class operationalSectorForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_operational_sector
        fields = "__all__"
        operational_area = ModelMultipleChoiceField(queryset=gnuhealth_operational_area.objects.values_list('name', flat=True), widget=Select2MultipleWidget)


class operationalAreaForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_operational_area
        fields = "__all__"

















        


        
# class phenotypeForm(forms.ModelForm):
#     class Meta:
#         model = gnuhealth_gene_varient_phenotype
#         fields = "__all__"
        
