from django.db import models

# Create your models here.
class gnuhealth_ethnicity(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    class Meta:
        db_table = 'gnuhealth_ethnicity'