from django.db import models

# Create your models here.
class gnuhealth_pathology(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    category = models.IntegerField()
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    protein = models.CharField(max_length=100)
    gene = models.CharField(max_length=100)
    chromosome = models.CharField(max_length=100)
    active = models.BooleanField()

    class Meta:
        db_table = 'gnuhealth_pathology'