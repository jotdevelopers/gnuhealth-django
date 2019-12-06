from django import forms
from health_demographics.models import *
from django.forms import ModelMultipleChoiceField
from health_configuration.models import *
from health_party.models import country_country, country_subdivision
from health_demographics.models import *
from health_operational_area.models import gnuhealth_operational_sector
from django_select2.forms import Select2MultipleWidget


class partyForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_du
        fields = "__all__"
        citizenship = ModelMultipleChoiceField(queryset=country_country.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        ethnicity = ModelMultipleChoiceField(queryset=gnuhealth_ethnicity.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        occupation = ModelMultipleChoiceField(queryset=gnuhealth_occupation.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        du = ModelMultipleChoiceField(queryset=gnuhealth_du.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        residence = ModelMultipleChoiceField(queryset=country_country.objects.values_list('name', flat=True), widget=Select2MultipleWidget)



