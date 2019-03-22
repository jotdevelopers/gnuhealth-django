from django.db import models

# Create your models here.

class gnuhealth_health_service(models.Model):
  id = models.IntegerField(primary_key=true)
  company = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  desc = models.CharField()
  institution = models.CharField()
  invoice_to = models.CharField()
  name = models.CharField()
  patient = models.CharField()
  service_date = models.DateField()
  state = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  insurance_holder = models.CharField()
  insurance_plan = models.CharField()
  
  
class gnuhealth_health_service_line(models.Model):
  id = models.IntegerField(primary_key=True)
  appointment = models.CharField()
  company = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  desc = models.CharField()
  from_date = models.DateField()
  name = models.CharField()
  product = models.CharField()
  qty = models.IntegerField()
  to_date = models.DateField()
  to_invoice = models.IntegerField()
  write_date = models.DateField()
  write_uid = models.IntegerField()

class Meta:
    db_table = 'gnuhealth_health_service'
    db_table = 'gnuhealth_health_service_line'