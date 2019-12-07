from django.db import models

# Create your models here.

class gnuhealth_immunization_schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    country = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    desc = models.CharField(max_length=100)
    sched = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    year = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_immunization_schedule'


class gnuhealth_immunization_schedule_dose(models.Model):
    id = models.IntegerField(primary_key=True)
    age_dose = models.IntegerField()
    age_unit = models.CharField(max_length=100)
    dose_number = models.IntegerField()
    remarks = models.CharField(max_length=100)
    vaccine = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()    
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_immunization_schedule_dose'


class gnuhealth_immunization_schedule_line(models.Model):
    id = models.IntegerField(primary_key=True)
    remarks = models.CharField(max_length=100)
    sched = models.IntegerField()
    scope = models.CharField(max_length=100)
    vaccine = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()    
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_immunization_schedule_line'