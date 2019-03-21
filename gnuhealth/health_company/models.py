from django.db import models

# Create your models here.

class company_company(models.Model):
  id = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  currency = models.IntegerField()
  footer = models.CharField()
  header = models.CharField()
  parent = models.CharField()
  party = models.CharField()
  timezone = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
  
class company_employee(models.Model):
  id = models.IntegerField()
  company = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  end_date = models.DateField()
  party = models.CharField()
  start_date = models.DateField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
