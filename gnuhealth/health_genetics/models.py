from django.db import models

# Create your models here.
<<<<<<< HEAD
class gnuhealth_gene_variant(models.Model):
    id = models.IntegerField()
    aa_change = models.CharField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    name = models.IntegerField()
    varient = models.CharField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_gene_variant_phenotype(models.Model):
    id = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    name = models.IntegerField()
    phenotype = models.IntegerField()
    varient = models.CharField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class Meta:
    db_table ='gnuhealth_gene_variant'
    db_table ='gnuhealth_gene_variant_phenotype'
=======

class gnuhealth_gene_variant(models.Model):
  id = models.IntegerField()
  aa_change = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  variant = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
>>>>>>> branch 'master' of https://github.com/jotdevelopers/gnuhealth-django.git
