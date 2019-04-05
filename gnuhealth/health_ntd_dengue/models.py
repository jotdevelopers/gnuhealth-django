from django.db import models

# Create your models here.

class gnuhealth_dengue_du_survey(models.Model):
    id = models.IntegerField(primary_key=True)
    aedes_larva = models.BooleanField()
    animal_water_container = models.BooleanField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    du = models.IntegerField()
    du_fumigation = models.BooleanField()
    du_status = models.CharField()
    larva_in_house = models.BooleanField()
    larva_peri = models.BooleanField()
    name = models.CharField()
    next_survey_date = models.DateField()
    observations = models.TextField()
    old_tyres = models.BooleanField()
    ovitraps = models.BooleanField()
    potted_plants = models.BooleanField()
    rock_holes = models.BooleanField()
    survey_date = models.DateField()
    tree_holes = models.BooleanField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class Meta:
    db_table = 'gnuhealth_dengue_du_survey'