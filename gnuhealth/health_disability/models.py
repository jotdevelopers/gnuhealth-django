from django.db import models

# Create your models here.
 class gnuhealth_patient_disability_assessment(models.Model):
    id = models.IntegerField(primary_key=True)
    activity_participation = models.CharField()
    assessment = models.CharField()
    assessment_date = models.DateField()
    cognitive_function = models.CharField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    crutches = models.BooleanField()
    hand_function = models.CharField()
    healthprof = models.IntegerField()
    hearing_function = models.CharField()
    locomotor_function = models.CharField()
    notes = models.TextField()
    patient = models.IntegerField()
    speech_function = models.CharField()
    visual_function = models.CharField()
    wheelchair = models.BooleanField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class Meta:
    db_table = 'gnuhealth_patient_disability_assessment'