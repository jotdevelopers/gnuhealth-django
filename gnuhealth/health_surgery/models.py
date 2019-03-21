from django.db import models

# Create your models here.

class gnuhealth_surgery(models.Model):
  id = models.IntegerField()
  admission = models.CharField()
  age = models.IntegerField()
  anesthesia_report = models.CharField()
  anesthetist = models.CharField()
  classification = models.CharField()
  code = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  description = models.CharField()
  extra_info = models.CharField()
  institution = models.CharField()
  operating_room = models.CharField()
  pathology = models.CharField()
  patient = models.CharField()
  postoperative_dx = models.CharField()
  preop_antibiotics = models.CharField()
  preop_asa = models.CharField()
  preop_bleeding_risk = models.CharField()
  preop_mallampati = models.CharField()
  preop_oximeter = models.CharField()
  preop_rci = models.CharField()
  preop_site_marketing = models.CharField()
  preop_sterility = models.CharField()
  signed_by = models.CharField()
  state = models.CharField()
  surgeon = models.CharField()
  surgeon_date = models.DateField()
  surgery_end_date = models.DateField()
  surgical_wound = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  main_procedure = models.CharField()
  
class gnuhealth_surgery_team(models.Model):
  id = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  notes = models.CharField()
  role = models.CharField()
  team_member = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  

class gnuhealth_surgery_supply(models.Model):
  id = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  notes = models.CharField()
  qty = models.IntegerField()
  qty_used = models.IntegerField()
  supply = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  





