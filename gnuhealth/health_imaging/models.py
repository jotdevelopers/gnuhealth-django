from django.db import models


# Create your models here.

<<<<<<< HEAD
class gnuhealth_imaging_test(models.Model):
    id = models.IntegerField()
    active = models.BooleanField()
    code = models.CharField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    name = models.CharField()
    product = models.IntegerField()
    test_type = models.IntegerField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class gnuhealth_imaging_test_request(models.Model):
    id = models.IntegerField()
    comment = models.TextField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    date = models.DateField()
    doctor = models.IntegerField()
    patient = models.IntegerField()
    request = models.CharField()
    requested_test = models.IntegerField()
    state = models.CharField()
    urgent = models.BooleanField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class gnuhealth_imaging_test_result(models.Model):
    id = models.IntegerField()
    comment = models.TextField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    date = models.DateField()
    doctor = models.IntegerField()
    number = models.IntegerField()
    patient = models.IntegerField()
    request = models.CharField()
    request_date = models.DateField()
    requested_test = models.IntegerField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class gnuhealth_imaging_test_type(models.Model):
    id = models.IntegerField()
    code = models.CharField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    name= models.CharField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class Meta:
    db_table = 'gnuhealth_imaging_test'
    db_table = 'gnuhealth_imaging_test_request'
    db_table = 'gnuhealth_imaging_test_result'
    db_table = 'gnuhealth_imaging_test_type'
=======
class gnuhealth_imaging_test_request(models.Model):
  id = models.IntegerField()
  comment = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  date = models.DateField()
  doctor = models.CharField()
  patient = models.CharField()
  request = models.CharField()
  requested_test = models.CharField()
  state = models.CharField()
  urgent = models.BooleanField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_imaging_test_type(models.Model):
  id = models.IntegerField()
  code = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_imaging_test_result(models.Model):
  id = models.IntegerField()
  comment = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  date = models.DateField()
  doctor = models.CharField()
  number = models.IntegerField()
  patient = models.CharField()
  request = models.CharField()
  requested_date = models.DateField()
  requested_test = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_imaging_test(models.Model):
  id = models.IntegerField()
  active = models.BooleanField()
  code = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  product = models.CharField()
  test_type = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
  
  
>>>>>>> branch 'master' of https://github.com/jotdevelopers/gnuhealth-django.git
