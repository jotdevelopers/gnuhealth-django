from django.db import models

# Create your models here.

class gnuhealth_patient_colposcopy_history(models.Model):
    id = models.IntegerField(primary_key=True)
    comments = models.CharField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    evaluation = models.IntegerField()
    evaluation_date = models.DateField()
    healthprof = models.IntegerField()
    institution = models.IntegerField()
    last_colposcopy = models.DateField()
    name = models.IntegerField()
    result = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class gnuhealth_patient_mammography_history(models.Model):
    id = models.IntegerField(primary_key=True)
    comments = models.CharField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    evaluation = models.IntegerField()
    evaluation_date = models.DateField()
    healthprof = models.IntegerField()
    institution = models.IntegerField()
    last_mammography = models.DateField()
    name = models.IntegerField()
    result = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class gnuhealth_patient_menstrual_history(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    dysmenorrhea = models.BooleanField()
    evaluation = models.IntegerField()
    evaluation_date = models.DateField()
    frequency = models.CharField()
    healthprof = models.IntegerField()
    institution = models.IntegerField()
    is_regular = models.BooleanField()
    lmp = models.DateField()
    lmp_length = models.IntegerField()
    name = models.IntegerField()
    volume = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class gnuhealth_patient_pap_history(models.Model):
    id = models.IntegerField(primary_key=True)
    comments = models.CharField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    evaluation = models.IntegerField()
    evaluation_date = models.DateField()
    healthprof = models.IntegerField()
    institution = models.IntegerField()
    last_pap = models.DateField()
    name = models.IntegerField()
    result = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
        
class Meta:
    db_table = 'gnuhealth_patient_colposcopy_history'
    db_table = 'gnuhealth_patient_mammography_history'
    db_table = 'gnuhealth_patient_menstrual_history'
    db_table = 'gnuhealth_patient_pap_history'