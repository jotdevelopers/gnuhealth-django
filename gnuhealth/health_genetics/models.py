from django.db import models
    
class gnuhealth_patient_genetic_risk(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    disease_gene = models.IntegerField()
    healthprof = models.IntegerField()
    institution = models.IntegerField()
    natural_variant = models.IntegerField()
    notes = models.CharField(max_length=100)
    onset = models.IntegerField()
    patient = models.IntegerField()
    variant_phenotype = models.IntegerField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    class Meta:
        db_table ='gnuhealth_patient_genetic_risk'
