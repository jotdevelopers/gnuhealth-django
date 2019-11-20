from django.db import models

# Create your models here.
class gnuhealth_appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    appointment_date = models.DateTimeField()
    appointment_type = models.CharField(max_length=100)
    checked_in_date = models.DateTimeField()
    comments = models.CharField(max_length=100)
    consultations = models.IntegerField()
    healthprof = models.IntegerField()
    institution = models.IntegerField()
    name = models.CharField(max_length=100)
    patient = models.IntegerField()
    speciality = models.IntegerField()
    state = models.CharField(max_length=100)
    urgency = models.CharField(max_length=100)
    visit_type = models.CharField(max_length=100)
    appointment_date_end = models.DateTimeField()
    event = models.IntegerField()
    inpatient_registration_code = models.IntegerField()

    class Meta:
        db_table = 'gnuhealth_appointment'