from django.db import models

# Create your models here.

class purchase_request(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    computing_quantity = models.IntegerField()
    computing_uom = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    description = models.CharField()
    exception_ignored = models.BooleanField()
    origin = models.CharField()
    party = models.IntegerField()
    number = models.CharField()
    party = models.IntegerField()
    product = models.IntegerField()
    purchase_date = models.DateField()
    purchase_line = models.IntegerField()
    state = models.CharField()
    stock_level = models.IntegerField()
    supply_date = models.DateField()
    uom = models.IntegerField()
    warehouse = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class Meta:
    db_table = 'purchase_request'
