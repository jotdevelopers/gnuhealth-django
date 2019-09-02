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
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    name = models.IntegerField()
    phenotype = models.IntegerField()
    varient = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class Meta:
    db_table ='gnuhealth_gene_variant'
    db_table ='gnuhealth_gene_variant_phenotype'
