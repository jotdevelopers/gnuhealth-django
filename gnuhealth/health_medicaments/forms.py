from django import forms
from django.forms import ModelMultipleChoiceField
from health_medicaments.models import *
from django_select2.forms import Select2MultipleWidget


class medicamentCategoryForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_medicament_category
        fields = ['id','name','parent','create_date', 'write_date']

class drugFormForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_drug_form
        fields = ['id','code','name','create_date', 'write_date']

class drugRouteForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_drug_route
        fields = ['id','code','name','create_date', 'write_date']

class doseUnitForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_dose_unit
        fields = ['id','desc','name','create_date', 'write_date']

class medicationDosageForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_medication_dosage
        fields = ['id','abbreviation','code','name','create_date', 'write_date']

class medicamentForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_medicament
        fields = ['id','active','active_component','adverse_reaction','category','composition','dosage','form','indications','is_vaccine','name','notes','overdosage','pregnancy','pregnancy_category','pregnancy_warning','presentation','route','sol_conc','sol_conc_unit','sol_vol','sol_vol_unit','storage','strength','therapeutic_action','unit','create_date', 'write_date', ]