from django.db import models

# Create your models here.

class calendar_calendar(models.Model):
  id = Models.IntegerField()
  create_date = models.DateField()
  create_uid = models.DateField()
  description = models.CharField()
  name = models.CharField()
  owner = models.CharField()
  write_date = models.DateField()
  write_uid = models.DateField()
  
class calendar_calendar-read-res_user(models.Model):
  id = models.IntegerField()
  calendar = models.DateField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  user = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class calendar_calendar-write-res_user(models.Model):
    id = models.IntegerField()
    calendar = models.DateField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    user = models.CharField()
    write_date = models.DateField()
    write_uid = models.IntegerField()
    
class calendar_category(models.Model):
  id = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  name = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class calendar_event(models.Model):
  id = models.IntegerField()
  all_day = models.IntegerField()
  calendar = models.DateField()
  classification = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  description = models.CharField()
  dtend = models.IntegerField()
  dtstart = models.IntegerField()
  location = models.CharField()
  organizer = models.CharField()
  parent = models.CharField()
  recurrence = models.CharField()
  sequence = models.CharField()
  status = models.BooleanField()
  summary = models.CharField()
  timezone = models.CharField()
  transp = models.CharField()
  uuid = models.CharField()
  vevent = models.CharField()
  write_date = models.DateField()
  write_uid = models.DateField()
  
class calendar_event-calendar_category(models.Model):
  id = models.IntegerField()
  category = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  event = models.CharField()
  write_date = models.DateField()
  write_uid = models.DateField()
  
  
