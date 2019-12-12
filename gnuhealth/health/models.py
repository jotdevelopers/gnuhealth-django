from django.db import models
from psycopg2.sql import DEFAULT

# Create your models here.from django.db import models

# Create your models here.

class gnuhealth_pol(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    create_date = models.CharField(max_length=100)
    create_uid = models.IntegerField()
    federation_account = models.CharField(max_length=100)
    gene = models.CharField(max_length=100)
    health_condition = models.CharField(max_length=100)
    health_condition_code = models.CharField(max_length=100)
    health_condition_text = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    medical_context = models.CharField(max_length=100)
    natural_variant = models.CharField(max_length=100)
    node = models.CharField(max_length=100)
    page = models.CharField(max_length=100)
    page_date = models.DateTimeField()
    page_type = models.CharField(max_length=100)
    person = models.IntegerField()
    phenotype = models.CharField(max_length=100)
    procedure = models.IntegerField()
    procedure_code = models.CharField(max_length=100)
    procedure_text = models.CharField(max_length=100)
    relevance = models.CharField(max_length=100)
    social_context = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    fsync = models.BooleanField()

    class Meta:
        db_table = 'gnuhealth_pol'
    
class gnuhealth_pathology(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    category = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    protein = models.CharField(max_length=100)
    gene = models.CharField(max_length=100)
    chromosome = models.CharField(max_length=100)
    active = models.BooleanField()

    class Meta:
        db_table = 'gnuhealth_pathology'




