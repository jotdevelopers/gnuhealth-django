from django.db import models

# Create your models here.
class gnuhealth_pol(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.CharField()
    author = models.CharField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    federation_account = models.CharField()
    gene = models.CharField()
    health_condition = models.ForeignKey(gnuhealth_pathology, on_delete=models.CASCADE)
    health_condition_code = models.CharField()
    health_condition_text = models.CharField()
    info = models.CharField()
    institution = models.ForeignKey(gnuhealth_institution, on_delete=models.CASCADE)
    medical_context = models.CharField()
    natural_varient = models.CharField()
    node = models.CharField()
    page = models.CharField()
    page_date = models.DateTimeField()
    page_type = models.CharField()
    person = models.IntegerField()
    phenotype = models.CharField()
    procedure = models.ForeignKey(gnuhealth_procedure, on_delete=models.CASCADE)
    procedure_code = models.CharField()
    procedure_text = models.CharField()
    relevance = models.CharField()
    social_context = models.CharField()
    summary = models.CharField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    fsync = models.BooleanField()
    
class gnuhealth_procedure(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    description = models.CharField()
    name = models.CharField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class gnuhealth_pathology(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    category = models.IntegerField()
    chromosome = models.CharField()
    code = models.CharField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    gene = models.CharField()
    info = models.CharField()
    name = models.CharField()
    protien = models.CharField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class gnuhealth_institution(models.Model):
    id = models.IntegerField(primary_key=True)
    beds = models.IntegerField()
    code = models.CharField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    extra_info = models.CharField()
    heliport = models.BooleanField()
    institution_type = models.CharField()
    name = models.ForeignKey(party_party, on_delete=models.CASCADE)
    operating_room = models.BooleanField()
    or_number = models.IntegerField()
    picture = models.ImageField()
    public_level = models.CharField()
    teaching = models.BooleanField()
    trauma_center = models.BooleanField()
    trauma_level = models.CharField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    main_speciality = models.IntegerField()
    
class party_party(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    code = models.CharField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    name = models.CharField()
    replaced_by = models.IntegerField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    activation_date = models.DateField()
    alternative_identification =  models.BooleanField()
    birth_certifcate = models.IntegerField()
    citizenship  models.IntegerField()
    death_certificate = models.IntegerField()
    deceased = models.BooleanField()
    dob= models.DateField()
    du = models.IntegerField()
    ethnic_group = models.IntegerField()
    fed_country = models.CharField()
    federation_account = models.CharField()
    gender = models.CharField()
    insurance_company_type = models.CharField()
    internal_user = models.IntegerField()
    is_healthprof = models.BooleanField()
    is_instituton = models.BooleanField()
    is_insurance_company = models.BooleanField()
    is_patient = models.BooleanField()
    is_person = models.BooleanField()
    is_pharmacy = models.BooleanField()
    lastname = models.CharField()
    marital_status = models.CharField()
    name_representation = models.CharField()
    photo = models.ImageField()
    ref = models.CharField()
    residence = models.IntegerField()
    unidentified = models.BooleanField()
    education = models.CharField()
    occupation = models.IntegerField()
    fsync = models.BooleanField()
    warehouse = models.IntegerField()


       
class Meta:
    db_table = 'gnuhealth_pol'
    db_table = 'gnuhealth_procedure'
    db_table = 'gnuhealth_pathology'
    db_table = 'gnuhealth_institution'
    db_table = 'party_party'




    
    
    
