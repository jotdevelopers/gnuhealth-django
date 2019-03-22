from django.db import models

# Create your models here.

class gnuhealth_paper_archive(models.Model):
  id = models.IntegerField(primary_key=True)
  comments = models.CharField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  create_location = models.CharField()
  hc_status = models.BooleanField()
  legacy = models.CharField()
  location = models.CharField()
  patient = models.CharField()
  request_date = models.DateTimeField()
  requested_by = models.CharField()
  return_date = models.DateTimeField()
  write_uid = models.IntegerField
  write_date = models.DateTimeField()

class Meta:
    db_table = 'gnuhealth_paper_archive'