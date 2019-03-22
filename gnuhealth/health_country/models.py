from django.db import models

# Create your models here.

class country_subdivision(models.Model):
  id = models.IntegerField(primary_key=True)
  code = models.IntegerField()
  country = models.CharField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  name =  models.CharField()
  parent = models.CharField()
  type = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class country_zip(models.Model):
  id = models.IntegerField(primary_key=True)
  city = models.CharField()
  country = models.CharField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  subdivision =  models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  zip = models.IntegerField()
  
class country_country(models.Model):
  id = models.IntegerField(primary_key=True)
  code = models.IntegerField()
  code3 = models.IntegerField()
  code_numeric = models.IntegerField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  name =  models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()

class Meta:
    db_table ='country_subdivision'
    db_table = 'country_zip'
    db_table = 'country_country'