from django import forms
from django.forms import ModelMultipleChoiceField
from health_imaging.models import *
from health_party.models import *
from health_health_professionals.models import *

from django_select2.forms import Select2MultipleWidget

class imagingResultForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_imaging_test_result
        fields = "__all__"
        doctor = ModelMultipleChoiceField(queryset=gnuhealth_healthprofessional.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        test = ModelMultipleChoiceField(queryset=gnuhealth_imaging_test.objects.values_list('name', flat=True), widget=Select2MultipleWidget)

class imagingRequestForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_imaging_test_result
        fields = "__all__"
        doctor = ModelMultipleChoiceField(queryset=gnuhealth_healthprofessional.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        test = ModelMultipleChoiceField(queryset=gnuhealth_imaging_test.objects.values_list('name', flat=True), widget=Select2MultipleWidget)


