from django.db import models

# Create your models here.

class gnuhealth_gene_variant(models.Model):
  id = models.IntegerField()
  aa_change = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  variant = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
