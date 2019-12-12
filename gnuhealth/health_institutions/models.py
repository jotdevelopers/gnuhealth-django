from django.db import models

# Create your models here.
class gnuhealth_institution(models.Model):
    id = models.IntegerField(primary_key=True)
    create_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    or_number = models.IntegerField()
    heliport = models.BooleanField()
    trauma_center = models.BooleanField()
    write_uid = models.IntegerField()
    beds = models.CharField(max_length=100)
    public_level = models.CharField(max_length=100)
    institution_type = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    operating_room = models.BooleanField()
    trauma_level = models.CharField(max_length=100)
    teaching = models.BooleanField()
    extra_info = models.CharField(max_length=100)
    main_specialty = models.CharField(max_length=100)

    class Meta:
        db_table = 'gnuhealth_institution'