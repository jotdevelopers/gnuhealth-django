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

class gnuhealth_procedure(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'gnuhealth_procedure'

class gnuhealth_institution(models.Model):
    id = models.IntegerField(primary_key=True)
    create_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    or_number = models.IntegerField()
    heliport = models.BooleanField()
    trauma_center = models.BooleanField()
    write_uid = models.IntegerField()
    beds = models.CharField(max_length=100)
    public_level = models.CharField(max_length=100)
    institution_type = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    operating_room = models.BooleanField()
    trauma_level = models.CharField(max_length=100)
    teaching = models.BooleanField()
    extra_info = models.CharField(max_length=100)
    main_specialty = models.CharField(max_length=100)

    class Meta:
        db_table = 'gnuhealth_institution'

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