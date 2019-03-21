from django.db import models

# Create your models here.

class gnuhealth_lab(models.Model):
  id = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  date_analysis = models.DateField()
  date_requested = models.DateField()
  diagnosis = models.CharField()
  name = models.CharField()
  pathologist = models.CharField()
  patient = models.CharField()
  request_order = models.CharField()
  requestor = models.CharField()
  results = models.CharField()
  test = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  digital_signature = models.CharField()
  document_digest = models.CharField()
  done_by = models.CharField()
  
  
class gnuhealth_lab_test_criteria(models.Model):
  id = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  excluded = models.CharField()
  gnuhealth_lab_id = models.IntegerField()
  lower_limit = models.IntegerField()
  name = models.CharField()
  normal_range = models.IntegerField()
  remarks = models.CharField()
  result = models.CharField()
  result_text = models.CharField()
  sequence = models.CharField()
  test_type_id = models.IntegerField()
  units = models.IntegerField()
  upper_limit = models.IntegerField()
  warning = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_lab_test_type(models.Model):
  id = models.IntegerField()
  active = models.BooleanField()
  code = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  info = models.CharField()
  name = models.CharField()
  product_id = models.IntegerField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
  
class gnuhealth_lab_test_units(models.Model):
  id = models.IntegerField()
  code = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
