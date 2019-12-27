from django import forms
from django.forms import ModelMultipleChoiceField
from health_prescriptions.models import *
from health_medicaments.models import *
from health_party.models import *
from django_select2.forms import Select2MultipleWidget

class prescriptionForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_prescription_order
        fields = "__all__"
  
class prescriptionLineForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_prescription_line
        fields = "__all__"
        medicament = ModelMultipleChoiceField(queryset=gnuhealth_medicament.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        dose_unit = ModelMultipleChoiceField(queryset=gnuhealth_dose_unit.objects.values_list('name', flat=True), widget=Select2MultipleWidget)


  #      country = ModelMultipleChoiceField(queryset=country_country.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
