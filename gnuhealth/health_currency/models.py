from django.db import models

# Create your models here.

class currency_currency_rate(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  currency = models.IntegerField()
  date = models.DateTimeField()
  rate = models.IntegerField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class currency_currency(models.Model):
  id = models.IntegerField(primary_key=True)
  active = models.BooleanField()
  code = models.IntegerField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  digits = models.IntegerField()
  mon_decimal_point = models.IntegerField()
  mon_grouping = models.CharField()
  mon_thousands_sep = models.CharField()
  n_cs_precedes = models.CharField()
  n_sep_by_space = models.CharField()
  n_sign_posn = models.CharField()
  name = models.CharField()
  negative_sign = models.CharField()
  numeric_code = models.CharField()
  p_cs_precedes = models.CharField()
  p_sep_by_space = models.CharField()
  p_sign_posn = models.CharField()
  positive_sign = models.CharField()
  rounding = models.CharField()
  symbol = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class Meta:
    db_table = 'currency_currency_rate'
    db_table = 'currency_currency'