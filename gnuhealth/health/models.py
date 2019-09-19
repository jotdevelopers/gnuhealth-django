from django.db import models
from psycopg2.sql import DEFAULT

# Create your models here.from django.db import models

# Create your models here.

class gnuhealth_pol(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    federation_account = models.CharField(max_length=100)
    health_condition_code = models.CharField(max_length=100)
    health_condition_text = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    node = models.CharField(max_length=100)
    page = models.CharField(max_length=100)
    person = models.IntegerField()
    procedure_code = models.CharField(max_length=100)
    procedure_text = models.CharField(max_length=100)
    relevance = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    

class Meta:
    db_table = 'gnuhealth_pol'
    
