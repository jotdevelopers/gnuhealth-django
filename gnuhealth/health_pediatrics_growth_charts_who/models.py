from django.db import models

# Create your models here.

class gnuhealth_pediatrics_growth_charts_who(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateField()
  create_uid = models.IntegerField()
  indicator = models.CharField()
  measure = models.CharField()
  month = models.CharField()
  sex = models.CharField()
  type = models.CharField()
  value = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()

class Meta:
    db_table = 'gnuhealth_pediatrics_growth_charts_who'