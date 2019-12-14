from django.db import models

# Create your models here.

class gnuhealth_healthprofessional(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateField()
    create_uid = models.IntegerField()
    active = models.BooleanField()
    code = models.CharField(max_length=100)
    institution = models.IntegerField()
    info = models.CharField(max_length=100)
    name = models.IntegerField()
    main_specialty = models.IntegerField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    class Meta:
        db_table ='gnuhealth_healthprofessional'
