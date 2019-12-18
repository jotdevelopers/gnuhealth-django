from django import forms
from django.forms import ModelMultipleChoiceField
from django_select2.forms import Select2MultipleWidget
from health_lab.models import *

class healthLabForm(forms.ModelForm):  
     class Meta:  
         model = gnuhealth_lab   
         fields = '__all__'

class requestLabForm(forms.ModelForm):  
     class Meta:  
         model = gnuhealth_lab   
         fields = '__all__'

class labTestUnitsForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_lab_test_units
        fields = ['id','code','name','create_date', 'write_date']


class labTestTypeForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_lab_test_type
        fields = ['id','active','code','info','name','product_id','create_date', 'write_date']