from django.db import models

# Create your models here.
            
class gnuhealth_operational_sector(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    info = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    operational_area = models.IntegerField()
    #operational_area = models.ForeignKey('gnuhealth_operational_area', db_column="operational_area", on_delete='')
    class Meta:
        db_table = 'gnuhealth_operational_sector'            

class gnuhealth_operational_area(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    info = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
   
    class Meta:
        db_table = 'gnuhealth_operational_area'