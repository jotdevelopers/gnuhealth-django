from django.db import models

# Create your models here.

class gnuhealth_federation_config(models.Model):
    write_uid = models.CharField(max_length=200)
    write_date = models.CharField(max_length=200)
    verify_ssl = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    ssl = models.CharField(max_length=200)
    port = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    id = models.IntegerField().primary_key
    host = models.CharField(max_length=200)
    enabled = models.CharField(max_length=200)
    create_uid = models.CharField(max_length=200)
    create_date = models.CharField(max_length=200)

class gnuhealth_federation_country_config(models.Model):
    country = models.CharField(max_length=200)
    create_date = models.CharField(max_length=200)
    create_uid = models.CharField(max_length=200)
    id = models.CharField(max_length=200)
    use_citizenship = models.CharField(max_length=200)
    write_date = models.CharField(max_length=200)
    write_uid  = models.CharField(max_length=200)
    
class gnuhealth_federation_object(models.Model):
    id = models.CharField(max_length=200)
    create_date = models.CharField(max_length=200)
    create_uid = models.CharField(max_length=200)
    enabled = models.CharField(max_length=200)
    fields = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    write_date = models.CharField(max_length=200)
    write_uid = models.CharField(max_length=200)
    
class gnuhealth_federation_queue(models.Model):
    id = models.CharField(max_length=200)
    args = models.CharField(max_length=200)
    create_date = models.CharField(max_length=200)
    create_uid = models.CharField(max_length=200)
    federation_locator = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    msgid = models.CharField(max_length=200)
    node = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    time_stamp = models.CharField(max_length=200)
    url_suffix = models.CharField(max_length=200)
    write_uid = models.CharField(max_length=200)
    write_date = models.CharField(max_length=200)
    
class Meta:
        db_table = 'gnuhealth_federation_config'
        db_table = 'gnuhealth_federation_country_config'
        db_table = 'gnuhealth_federation_object'
        db_table = 'gnuhealth_federation_queue'
    
