from django.db import models

# Create your models here.

class gnuhealth_medicament_category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    parent = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_medicament_category'

class gnuhealth_drug_form(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_drug_form'

class gnuhealth_drug_route(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_drug_route'

class gnuhealth_dose_unit(models.Model):
    id = models.IntegerField(primary_key=True)
    desc = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_dose_unit'

class gnuhealth_medication_dosage(models.Model):
    id = models.IntegerField(primary_key=True)
    abbreviation = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_medication_dosage'

class gnuhealth_medicament(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    active_component = models.CharField(max_length=100)
    adverse_reaction = models.CharField(max_length=100)
    category = models.IntegerField()
    composition = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    form = models.IntegerField()
    indications = models.CharField(max_length=100)
    is_vaccine = models.BooleanField()
    name = models.IntegerField()
    notes = models.CharField(max_length=100)
    overdosage = models.CharField(max_length=100)
    pregnancy = models.CharField(max_length=100)
    pregnancy_category = models.CharField(max_length=100)
    pregnancy_warning = models.BooleanField()
    presentation = models.CharField(max_length=100)
    route = models.IntegerField()
    sol_conc = models.FloatField()
    sol_conc_unit = models.IntegerField()
    sol_vol = models.FloatField()
    sol_vol_unit = models.IntegerField()
    storage = models.CharField(max_length=100)
    strength = models.FloatField()
    therapeutic_action = models.CharField(max_length=100)
    unit = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_medicament'
