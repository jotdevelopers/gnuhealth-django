from django import forms
from django.forms import ModelMultipleChoiceField
from health_immunization_schedule.models import *
from django_select2.forms import Select2MultipleWidget


class immunizationScheduleForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_immunization_schedule
        fields = ['id','country','desc','sched','year', 'active', 'create_date', 'write_date']

class vaccineDosesForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_immunization_schedule_dose
        fields = ['id','age_dose','age_unit','dose_number','remarks', 'vaccine', 'create_date', 'write_date']

class scheduleLineForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_immunization_schedule_line
        fields = ['id','remarks','sched','scope','vaccine','create_date', 'write_date']