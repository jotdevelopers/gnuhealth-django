from django.db import models

# Create your models here.

class gnuhealth_insurance(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField()
    company = models.CharField()
    create_date = models.DateField(max_length=6)
    create_uid = models.IntegerField()
    insurance_type = models.CharField()
    member_exp = models.DateField()
    member_since = models.DateField()
    name = models.CharField()
    notes = models.TextField()
    number = models.CharField()
    plan_id = models.IntegerField()
    write_date = models.CharField()
    write_uid = models.IntegerField()
    
class gnuhealth_insurance_plan(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.CharField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    is_default = models.BooleanField()
    name = models.CharField()
    notes = models.CharField()
    write_date = models.CharField()
    write_uid = models.IntegerField()
  
class gnuhealth_insurance_plan_product_policy(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    discount = models.IntegerField()
    plan = models.CharField()
    product = models.CharField()
    product_category = models.CharField()
    write_date = models.CharField()
    write_uid = models.IntegerField()

class Meta:
    db_table = 'gnuhealth_insurance'
    db_table = 'gnuhealth_insurance_plan'
    db_table = 'gnuhealth_insurance_plan_product_policy'