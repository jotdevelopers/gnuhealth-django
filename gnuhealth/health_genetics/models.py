from django.db import models

# Create your models here.
class gnuhealth_gene_variant(models.Model):
    id = models.IntegerField(primary_key=True)
    aa_change = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    name = models.IntegerField()
    varient = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_gene_variant_phenotype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.IntegerField()
    phenotype = models.IntegerField()
    varient = models.CharField(max_length=100)
    
class gnuhealth_patient_genetic_risk(models.Model):
    id = models.IntegerField(primary_key=True)
    #create_date = models.DateField()
    #create_uid = models.IntegerField()
    disease_gene = models.IntegerField()
    healthprof = models.IntegerField()
    #institution = models.IntegerField()
    natural_varient = models.IntegerField()
    notes = models.CharField(max_length=100)
    onset = models.IntegerField()
    patient = models.IntegerField()
    varient_phenotype = models.IntegerField()
    #write_date = models.DateField()
    #write_uid = models.IntegerField()

class Meta:
    db_table ='gnuhealth_gene_variant'
    db_table ='gnuhealth_gene_variant_phenotype'
