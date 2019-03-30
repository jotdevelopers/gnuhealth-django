from django.db import models

# Create your models here.
class stock_lot(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    number = models.CharField()
    product = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    expiration_date = models.DateField()
    
class stock_lot_type(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    name = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class Meta:
    db_table = 'stock_lot'
    db_table = 'stock_lot_type'