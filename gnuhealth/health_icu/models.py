from django.db import models

# Create your models here.

class gnuhealth_icu_apache2(models.Model):
    id = models.IntegerField()
    aado2 = models.IntegerField()
    age = models.IntegerField()
    apache_score = models.IntegerField()
    arf = models.BooleanField()
    chronic_condition = models.BooleanField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    fio2 = models.IntegerField()
    gcs = models.IntegerField()
    heart_rate = models.IntegerField()
    hematocrit = models.IntegerField()
    hospital_admission_type = models.CharField()
    mean_ap = models.IntegerField()
    name = models.IntegerField()
    paco2 = models.IntegerField()
    pao2 = models.IntegerField()
    ph = models.IntegerField()
    respiratory_rate = models.IntegerField()
    score_date = models.DateTimeField()
    serum_creatinine = models.IntegerField()
    serum_potassium = models.IntegerField()
    serum_sodium = models.IntegerField()
    temperature = models.IntegerField()
    wbc = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_icu_chest_drainage(models.Model):
    id = models.IntegerField()
    air_leak = models.BooleanField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    fluid_aspect = models.CharField()
    fluid_volume = models.IntegerField()
    location = models.CharField()
    name = models.IntegerField()
    oscillation = models.BooleanField()
    remarks = models.CharField()
    suction = models.BooleanField()
    suction_pressure = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_icu_glasgow(models.Model):
    id = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    evaluation_date = models.DateTimeField()
    glasgow = models.IntegerField()
    glasgow_eyes = models.CharField()
    glasgow_motor = models.CharField()
    glasgow_verbal = models.CharField()
    name = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_icu_ventilation(models.Model):
    id = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    current_mv = models.BooleanField()
    ett_size = models.IntegerField()
    mv_end = models.DateTimeField()
    mv_start = models.DateTimeField()
    name = models.IntegerField()
    remarks = models.CharField()
    tracheostomy_size  models.IntegerField()
    ventilation = models.CharField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class Meta:
    db_table = 'gnuhealth_icu_apache2'
    db_table = 'gnuhealth_icu_chest_drainage'
    db_table = 'gnuhealth_icu_glasgow'
    db_table = 'gnuhealth_icu_ventilation'