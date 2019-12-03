from django import forms
from health_demographics.models import *
from django.forms import ModelMultipleChoiceField
from health_configuration.models import *
from health_party.models import *
from django_select2.forms import Select2MultipleWidget

class familyForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_family
        fields = "__all__"
        
class familyMemberForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_family_member
        fields = "__all__"
        
class duForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_du
        fields = "__all__"
        address_country = ModelMultipleChoiceField(queryset=country_country.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        address_subdivision = ModelMultipleChoiceField(queryset=country_subdivision.objects.values_list('name', flat=True), widget=Select2MultipleWidget)



