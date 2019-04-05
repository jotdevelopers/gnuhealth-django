from django.db import models

# Create your models here.

class gnuhealth_surgery(models.Model):
    id = models.IntegerField(primary_key=True)
    admission = models.IntegerField()
    age = models.CharField()
    anesthesia_report = models.TextField()
    anesthetist = models.IntegerField()
    classification = models.CharField()
    code = models.CharField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    description = models.CharField()
    extra_info = models.TextField()
    institution = models.IntegerField()
    operating_room = models.IntegerField()
    pathology = models.IntegerField()
    patient = models.IntegerField()
    postoperative_dx = models.IntegerField()
    preop_antibiotics = models.BooleanField()
    preop_asa = models.CharField()
    preop_bleeding_risk = models.BooleanField()
    preop_mallampati = models.CharField()
    preop_oximeter = models.BooleanField()
    preop_rcri = models.IntegerField()
    preop_site_marking = models.BooleanField()
    preop_sterility = models.BooleanField()
    signed_by = models.IntegerField()
    state = models.CharField()
    surgeon = models.IntegerField()
    surgery_date = models.DateField()
    surgery_end_date = models.DateField()
    surgical_wound = models.CharField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    main_procedure = models.IntegerField()
    
class gnuhealth_surgery_supply(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    name = models.IntegerField()
    notes = models.CharField()
    qty = models.IntegerField()
    qty_used = models.IntegerField()
    supply = models.IntegerField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class gnuhealth_surgery_team(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    name = models.IntegerField()
    notes = models.CharField()
    roles = models.IntegerField()
    team_member = models.IntegerField()
    supply = models.IntegerField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class Meta:
    db_table = 'gnuhealth_surgery'
    db_table = 'gnuhealth_surgery_supply'
    db_table = 'gnuhealth_surgery_team'
