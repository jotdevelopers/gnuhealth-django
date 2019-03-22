from django.db import models

# Create your models here.

class gnuhealth_chagas_du_survey(models.Model):
    id = models.IntegerField(primary_key=True)
    bugtraps = models.BooleanField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    dfloor = models.BooleanField()
    dperi = models.BooleanField()
    droof = models.BooleanField()
    du = models.IntegerField()
    du_fumigation = models.BooleanField()
    du_paint = models.BooleanField()
    du_status = models.CharField()
    dwall = models.BooleanField()
    fumigation_date = models.DateField()
    name = models.CharField()
    next_survey_date = models.DateField()
    nymphs = models.BooleanField()
    observations = models.TextField()
    paint_date = models.DateField()
    survey_date = models.DateField()
    t_in_house = models.BooleanField()
    t_peri = models.BooleanField()
    triatomines = models.BooleanField()
    vector = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class Meta:
    db_table = 'gnuhealth_chagas_du_survey'