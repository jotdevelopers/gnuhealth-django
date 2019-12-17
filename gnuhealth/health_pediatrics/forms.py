from django import forms
from django.forms import ModelMultipleChoiceField
from django_select2.forms import Select2MultipleWidget
from health_pediatrics.models import *


class newBornForm(forms.ModelForm):
    class Meta:
        model = gnuhealth_newborn
        fields = ['id','apgar1','apgar5','bd','birth_date','cephalic_perimeter','cod','died_at_delivery','died_at_the_hospital','died_being_transferred','dismissed','healthprof','length','meconium','mother','name','neonatal_ambiguous_genitalia','neonatal_babinski_reflex','neonatal_barlow','neonatal_blink_reflex','neonatal_erbs_palsy','neonatal_grasp_reflex','neonatal_hematoma','neonatal_hernia','neonatal_moro_reflex','neonatal_ortolani','neonatal_palmar_crease','neonatal_polydactyly','neonatal_rooting_reflex','neonatal_stepping_reflex','neonatal_sucking_reflex','neonatal_swimming_reflex','neonatal_syndactyly','neonatal_talipes_equinovarus','neonatal_tonic_neck_reflex','newborn_name','notes','patient','reanimation_aspiration','reanimation_mask','reanimation_oxygen','reanimation_stimulation','sex','signed_by','state','test_audition','test_billirubin','test_chagas','test_metabolic','test_toxo','test_vdrl','tod','weight','create_date','write_date']