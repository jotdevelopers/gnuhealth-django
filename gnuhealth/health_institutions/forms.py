from django import forms
from django.forms import ModelMultipleChoiceField
from health_institutions.models import *
from health_party.models import *
from django_select2.forms import Select2MultipleWidget

class institutionForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_institution
        fields = "__all__"
        name = ModelMultipleChoiceField(queryset=party_party.objects.values_list('name', flat=True), widget=Select2MultipleWidget)

