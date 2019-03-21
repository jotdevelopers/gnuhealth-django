from django.db import models

# Create your models here.

class gnuhealth_imaging_test_request(models.Model):
  id = models.IntegerField()
  comment = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  date = models.DateField()
  doctor = models.CharField()
  patient = models.CharField()
  request = models.CharField()
  requested_test = models.CharField()
  state = models.CharField()
  urgent = models.BooleanField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_imaging_test_type(models.Model):
  id = models.IntegerField()
  code = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_imaging_test_result(models.Model):
  id = models.IntegerField()
  comment = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  date = models.DateField()
  doctor = models.CharField()
  number = models.IntegerField()
  patient = models.CharField()
  request = models.CharField()
  requested_date = models.DateField()
  requested_test = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_imaging_test(models.Model):
  id = models.IntegerField()
  active = models.BooleanField()
  code = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  product = models.CharField()
  test_type = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
  
  
