from django.db import models

# Create your models here.

class company_company(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  currency = models.IntegerField()
  footer = models.CharField()
  header = models.CharField()
  parent = models.CharField()
  party = models.CharField()
  timezone = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
  
class company_employee(models.Model):
  id = models.IntegerField(primary_key=True)
  company = models.CharField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  end_date = models.DateTimeField()
  party = models.CharField()
  start_date = models.DateTimeField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class Meta:
    db_table = 'company_company'
    db_table = 'company_employee'