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


class country(models.Model):
    class stock_location(models.Model):

        class gnuhealth_birth_certificate(models.Model):

        class gnuhealth_du(models.Model):