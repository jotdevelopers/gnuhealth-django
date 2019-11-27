from django.db import models

# Create your models here.

        
class gnuhealth_death_certificate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    autopsy = models.BooleanField()
    code = models.CharField(max_length=100)
    country = models.IntegerField()
    country_subdivision = models.IntegerField()
    dod = models.DateField()
    du = models.IntegerField()
    name = models.IntegerField()
    observations = models.CharField(max_length=100)
    operational_sector = models.IntegerField()
    place_details = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    type_of_death = models.CharField(max_length=100)
    certification_date = models.DateTimeField()
    cod = models.IntegerField()
    institution = models.IntegerField()
    signed_by = models.IntegerField()
    digital_signature = models.CharField(max_length=100)
    document_digest = models.CharField(max_length=100)
    serializer = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_death_certificate'

class gnuhealth_family(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_family'
    
class gnuhealth_family_member(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.IntegerField()
    party= models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_family_member'
        