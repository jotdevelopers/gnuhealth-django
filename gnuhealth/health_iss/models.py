from django.db import models

# Create your models here.

class gnuhealth_iss(models.Model):
  id = models.IntegerField(primary_key=True)
  alchohol = models.CharField()
  code = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  disposition = models.CharField()
  drugs = models.CharField()
  healthcenter = models.CharField()
  injury_date = models.DateField()
  injury_details = models.CharField()
  injury_method = models.CharField()
  injury_type = models.CharField()
  latitude = models.CharField()
  longitude = models.CharField()
  mva_counterpart = models.CharField()
  mva_mode = models.CharField()
  mva_position = models.CharField()
  name = models.CharField()
  operational_sector = models.CharField()
  pace_occurence = models.IntegerField()
  registration_date = models.DateField()
  safety_gear = models.CharField()
  urladdr  = models.CharField()
  victim_prepetrator = models.CharField()
  violence_circumstances = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()

class Meta:
    db_table = 'gnuhealth_iss'