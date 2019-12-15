from django.db import models
from datetime import datetime

# Create your models here.

class gnuhealth_newborn(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    write_date = models.DateTimeField(null=True, blank=True)
    create_uid = models.IntegerField(null=True, blank=True)
    write_uid = models.IntegerField(null=True, blank=True)
    apgar1 = models.IntegerField(null=True, blank=True)
    apgar5 = models.IntegerField(null=True, blank=True)
    bd = models.BooleanField(null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    cephalic_perimeter = models.IntegerField(null=True, blank=True)
    cod = models.IntegerField(null=True, blank=True)
    died_at_delivery = models.BooleanField(null=True, blank=True)
    died_at_the_hospital = models.BooleanField(null=True, blank=True)
    died_being_transferred = models.BooleanField(null=True, blank=True)
    dismissed = models.DateTimeField(null=True, blank=True)
    healthprof = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    meconium = models.BooleanField(null=True, blank=True)
    mother = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    neonatal_ambiguous_genitalia = models.BooleanField(null=True, blank=True)
    neonatal_babinski_reflex = models.BooleanField(null=True, blank=True)
    neonatal_barlow = models.BooleanField(null=True, blank=True)
    neonatal_blink_reflex = models.BooleanField(null=True, blank=True)
    neonatal_erbs_palsy = models.BooleanField(null=True, blank=True)
    neonatal_grasp_reflex = models.BooleanField(null=True, blank=True)
    neonatal_hematoma = models.BooleanField(null=True, blank=True)
    neonatal_hernia = models.BooleanField(null=True, blank=True)
    neonatal_moro_reflex = models.BooleanField(null=True, blank=True)
    neonatal_ortolani = models.BooleanField(null=True, blank=True)
    neonatal_palmar_crease = models.BooleanField(null=True, blank=True)
    neonatal_polydactyly = models.BooleanField(null=True, blank=True)
    neonatal_rooting_reflex = models.BooleanField(null=True, blank=True)
    neonatal_stepping_reflex = models.BooleanField(null=True, blank=True)
    neonatal_sucking_reflex = models.BooleanField(null=True, blank=True)
    neonatal_swimming_reflex = models.BooleanField(null=True, blank=True)
    neonatal_syndactyly = models.BooleanField(null=True, blank=True)
    neonatal_talipes_equinovarus = models.BooleanField(null=True, blank=True)
    neonatal_tonic_neck_reflex = models.BooleanField(null=True, blank=True)
    newborn_name = models.CharField(max_length=100, null=True, blank=True)
    notes = models.CharField(max_length=100, null=True, blank=True)
    patient = models.IntegerField(null=True, blank=True)
    photo = models.BinaryField(max_length=None, null=True, blank=True)
    reanimation_aspiration = models.BooleanField(null=True, blank=True)
    reanimation_mask = models.BooleanField(null=True, blank=True)
    reanimation_oxygen = models.BooleanField(null=True, blank=True)
    reanimation_stimulation = models.BooleanField(null=True, blank=True)
    sex = models.CharField(max_length=100, null=True, blank=True)
    signed_by = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    test_audition = models.BooleanField(null=True, blank=True)
    test_billirubin = models.BooleanField(null=True, blank=True)
    test_chagas = models.BooleanField(null=True, blank=True)
    test_metabolic = models.BooleanField(null=True, blank=True)
    test_toxo = models.BooleanField(null=True, blank=True)
    test_vdrl = models.BooleanField(null=True, blank=True)
    tod = models.DateTimeField(null=True, blank=True)
    weight = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_newborn'