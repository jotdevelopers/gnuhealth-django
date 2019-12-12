from django.db import models
from health_configuration.models import *
from health_party.models import country_country, country_subdivision
from health_demographics.models import *
from health_operational_area.models import gnuhealth_operational_sector
from health_demographics.models import *

# Create your models here.
class gnuhealth_du(models.Model):
    id = models.IntegerField(primary_key=True)
    address_city = models.CharField(max_length=100)
    address_country = models.IntegerField()
    address_district = models.CharField(max_length=100)
    address_municipality = models.CharField(max_length=100)
    address_street = models.CharField(max_length=100)
    address_street_bis = models.CharField(max_length=100)
    address_street_number = models.IntegerField()
    address_subdivision =  models.IntegerField()
    address_zip = models.CharField(max_length=100)
    altitude = models.IntegerField()
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    desc = models.CharField(max_length=100)
    dwelling = models.CharField(max_length=100)
    electricity = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    housing = models.CharField(max_length=100)
    internet = models.BooleanField(default=False)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    materials = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    operational_sector = models.IntegerField()
    picture = models.CharField(max_length=100)
    roof_type = models.CharField(max_length=100)
    sewers = models.BooleanField(default=False)
    telephone = models.BooleanField(default=False)
    television = models.BooleanField(default=False)
    total_surface = models.IntegerField()
    trash = models.BooleanField(default=False)
    urladdr = models.CharField(max_length=100)
    water = models.BooleanField(default=False)
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_du'
             
        
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
    place_of_death = models.CharField(max_length=100)
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

class gnuhealth_birth_certificate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    country = models.IntegerField()
    country_subdivision = models.IntegerField()
    dob = models.DateField()
    du = models.IntegerField()
    father = models.IntegerField()
    mother = models.IntegerField()
    observations = models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    certification_date = models.DateTimeField()
    cod = models.IntegerField()
    institution = models.IntegerField()
    signed_by = models.IntegerField()
    digital_signature = models.CharField(max_length=100)
    document_digest = models.CharField(max_length=100)
    serializer = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_birth_certificate'


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
        
        
