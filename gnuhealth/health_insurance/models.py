from django.db import models

# Create your models here.

class gnuhealth_insurance_plan(models.Model):
  id = models.IntegerField()
  company = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  is_default = models.BooleanField()
  name = models.CharField()
  notes = models.CharField()
  write_date = models.CharField()
  write_uid = models.IntegerField()
  
class gnuhealth_insurance_plan_product_policy(models.Model):
  id = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  discount = models.IntegerField()
  plan = models.CharField()
  product = models.CharField()
  product_category = models.CharField()
  write_date = models.CharField()
  write_uid = models.IntegerField()
