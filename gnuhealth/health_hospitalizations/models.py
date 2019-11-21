from django.db import models


# Create your models here.
class gnuhealth_inpatient_meal_order(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    health_professional = models.IntegerField()
    meal_order = models.CharField(max_length=100)
    meal_warning = models.BooleanField()
    meal_warning_ack = models.BooleanField()
    mealtime = models.CharField(max_length=100)
    name = models.IntegerField()
    order_date = models.DateTimeField()
    remarks = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        db_table = 'gnuhealth_inpatient_meal_order'
