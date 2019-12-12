from django.db import models
from health_configuration.models import *


# Create your models here.
class party_party(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    code = models.CharField(max_length=100)
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

class party_address(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    active = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    country = models.IntegerField()
    name = models.CharField(max_length=100)
    party = models.IntegerField()
    sequence = models.IntegerField()
    street = models.CharField(max_length=100)
    subdivision = models.IntegerField()
    zip = models.CharField(max_length=100)
    delivery = models.BooleanField(default=False)
    is_school = models.BooleanField(default=False)
    is_work = models.BooleanField(default=False)
    relationship = models.CharField(max_length=100)
    relative_id = models.IntegerField()
    invoice = models.BooleanField(default=False)

    class Meta:
        db_table = 'party_address'

class party_address_format(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    active = models.BooleanField(default=False)
    country = models.IntegerField()
    format_i = models.CharField(max_length=100)
    language = models.IntegerField()

    class Meta:
        db_table = 'party_address_format'

class party_category(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    parent = models.IntegerField()

    class Meta:
        db_table = 'party_category'

class party_category_rel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    category = models.IntegerField()
    party = models.IntegerField()

    class Meta:
        db_table = 'party_category_rel'

class party_configuration(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()

    class Meta:
        db_table = 'party_configuration'

class party_configuration_party_lang(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    party_lang = models.IntegerField()
    company = models.IntegerField()

    class Meta:
        db_table = 'party_configuration_party_lang'

class party_configuration_party_sequence(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    party_sequence = models.IntegerField()

    class Meta:
        db_table = 'party_configuration_party_sequence'

class party_contact_mechanism(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    active = models.BooleanField(default=False)
    party = models.IntegerField()
    sequence = models.IntegerField()
    type = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    value_compact = models.CharField(max_length=100)
    emergency = models.BooleanField(default=False)
    remarks = models.CharField(max_length=100)

    class Meta:
        db_table = 'party_contact_mechanism'


class party_idetifier(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    party = models.IntegerField()
    sequence = models.IntegerField()
    type = models.CharField(max_length=100)

    class Meta:
        db_table = 'party_idetifier'

class party_party_account(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    account_payable = models.IntegerField()
    account_recievable = models.IntegerField()
    customer_tax_rule = models.IntegerField()
    party = models.IntegerField()
    supplier_tax_rule = models.IntegerField()

    class Meta:
        db_table = 'party_party_account'

class party_party_lang(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    language = models.IntegerField()
    party = models.IntegerField()
    company = models.IntegerField()

    class Meta:
        db_table = 'party_party_lang'

class party_party_location(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    customer_location = models.IntegerField()
    party = models.IntegerField()
    supplier_location = models.IntegerField()

    class Meta:
        db_table = 'party_party_location'

class party_party_payment_term(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    customer_payment_term = models.IntegerField()
    party = models.IntegerField()
    supplier_payment_term = models.IntegerField()

    class Meta:
        db_table = 'party_party_payment_term'

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


class country_subdivision(models.Model):
    id = models.IntegerField(primary_key=True)    
    code = models.CharField(max_length=100)
    country = models.ForeignKey('country_country', db_column="country", on_delete='')
    name = models.CharField(max_length=100)
    parent = models.IntegerField()
    type = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'country_subdivision'