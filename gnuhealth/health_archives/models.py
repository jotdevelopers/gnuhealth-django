from django.db import models

# Create your models here.


class gnuhealth_paper_archive(models.Model):
  id = models.IntegerField()
  comments = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  create_location = models.CharField()
  hc_status = models.BooleanField()
  legacy = models.CharField()
  location = models.CharField()
  patient = models.CharField()
  request_date = models.DateField()
  requested_by = models.CharField()
  return_date = models.DateField()
  write_uid = models.IntegerField
  write_date = models.DateField()
