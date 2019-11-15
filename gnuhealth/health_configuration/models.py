from django.db import models

# Create your models here.
class gnuhealth_ethnicity(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_ethnicity'
        
        
class gnuhealth_occupation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_occupation'

class gnuhealth_disease_genes(models.Model):
      id = models.IntegerField(primary_key=True)
      chromosome = models.CharField(max_length = 100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      gene_id = models.CharField(max_length = 100)
      info = models.CharField(max_length=100)
      location = models.CharField(max_length = 100)
      long_name = models.CharField(max_length = 100)
      name = models.CharField(max_length=100)
      protein_name = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
             db_table = 'gnuhealth_disease_gene'
             
class gnuhealth_gene_varient(models.Model):
      id = models.IntegerField(primary_key=True)
      aa_change = models.CharField(max_length = 100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      name = models.IntegerField()
      varient = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
             db_table = 'gnuhealth_gene_varient'             
