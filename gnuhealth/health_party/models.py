from django.db import models

# Create your models here.
class party_party(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    code_length = models.IntegerField()
    active = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    alternative_identification = models.CharField(max_length=100)
    is_healthprof = models.BooleanField()
    insurance_company_type = models.CharField(max_length=100)
    internal_user = models.IntegerField()
    activation_date = models.DateTimeField()
    citizenship = models.IntegerField()
    is_patient = models.BooleanField()
    is_insurance_company = models.BooleanField()
    ref = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    ethnic_group = models.IntegerField()
    du = models.IntegerField()
    unidentified = models.BooleanField()
    dob = models.DateTimeField()
    is_institution = models.BooleanField()
    marital_status = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    is_pharmacy = models.BooleanField()
    residence = models.IntegerField()
    is_person = models.BooleanField()
    education = models.CharField(max_length=100)
    occupation = models.IntegerField()
    warehouse = models.IntegerField()
    death_certificate = models.IntegerField()
    birth_certificate = models.IntegerField()
    deceased = models.BooleanField()
    name_representation = models.CharField(max_length=100)
    replaced_by = models.IntegerField()
    federation_account = models.CharField(max_length=100)
    fed_country = models.CharField(max_length=100)
    fsync = models.BooleanField()
    class Meta:
        db_table = 'party_party'


class country_country(models.Model):
    id = models.IntegerField(primary_key=True)    
    code = models.CharField(max_length=100)
    code3 = models.CharField(max_length=100)
    code_numeric = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'country_country'

class stock_location(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    address = models.IntegerField()
    code = models.CharField(max_length=100)
    flat_childs = models.BooleanField()
    input_location = models.IntegerField()
    left = models.IntegerField()
    name = models.CharField(max_length=100)
    output_location = models.IntegerField()
    parent = models.IntegerField()
    picking_location = models.IntegerField()
    right = models.IntegerField()
    storage_location = models.IntegerField()
    type = models.CharField(max_length=100)
    supplier_return_location = models.IntegerField()
    overflowing_location = models.IntegerField()
    provisioning_location = models.IntegerField()
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'stock_location'

class gnuhealth_birth_certificate(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=100)
    country = models.IntegerField()
    country_subdivision = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    dob = models.DateTimeField()
    father = models.IntegerField()
    mother = models.IntegerField()
    name = models.IntegerField()
    observations = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    certification_date = models.DateTimeField()
    institution = models.IntegerField()
    signed_by = models.IntegerField()
    digital_signature = models.CharField(max_length=100)
    document_digest = models.CharField(max_length=100)
    serializer = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_birth_certificate'




class country_subdivision(models.Model):
    id = models.IntegerField(primary_key=True)    
    code = models.CharField(max_length=100)
    country = models.IntegerField()
    name = models.CharField(max_length=100)
    parent = models.IntegerField()
    type = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'country_subdivision'