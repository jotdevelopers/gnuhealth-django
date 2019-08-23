from django.db import models

# Create your models here.

class gnuhealth_lab(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    date_analysis = models.DateField()
    date_requested = models.DateField()
    diagnosis = models.TextField()
    name = models.CharField(max_length=200)
    pathologist = models.IntegerField()
    patient = models.IntegerField()
    request_order = models.IntegerField()
    requester = models.IntegerField()
    results = models.TextField()
    test = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    digital_signature = models.TextField()
    document_digest = models.CharField(max_length=200)
    done_by = models.IntegerField()
    done_date = models.DateTimeField()
    serializer = models.TextField()
    state = models.CharField(max_length=200)
    validated_by = models.IntegerField()
    validation_date = models.DateField()
    
class gnuhealth_lab_test_critearea(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    excluded = models.BooleanField()
    gnuhealth_lab_id = models.IntegerField()
    lower_limit = models.IntegerField()
    name = models.CharField(max_length=200)
    normal_range = models.TextField()
    remarks = models.CharField(max_length=200)
    result = models.IntegerField()
    result_text = models.CharField(max_length=200)
    sequence = models.IntegerField()
    test_type_id = models.IntegerField()
    units = models.IntegerField()
    upper_limit = models.IntegerField()
    warning = models.BooleanField()
    write_date = models.DateField()
    wrte_uid = models.IntegerField()
    
class gnuhealth_lab_test_type(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    code = models.CharField(max_length=200)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    info = models.TextField()
    name = models.CharField(max_length=200)
    product_id = models.IntegerField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class gnuhealth_lab_test_units(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=200)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    name = models.CharField(max_length=200)
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class Meta:
    db_table = 'gnuhealth_lab'
    db_table = 'gnuhealth_lab_test_critearea'
    db_table = 'gnuhealth_lab_test_type'
    db_table = 'gnuhealth_lab_test_units'
