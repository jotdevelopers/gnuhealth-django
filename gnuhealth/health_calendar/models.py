from django.db import models

# Create your models here.

class calendar_calendar(models.Model):
  id = Models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.DateTimeField()
  description = models.CharField()
  name = models.CharField()
  owner = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.DateTimeField()
  
class calendar_calendar-read-res_user(models.Model):
  id = models.IntegerField(primary_key=True)
  calendar = models.DateTimeField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  user = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class calendar_calendar-write-res_user(models.Model):
    id = models.IntegerField(primary_key=True)
    calendar = models.DateTimeField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    user = models.CharField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class calendar_category(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  name = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class calendar_event(models.Model):
  id = models.IntegerField(primary_key=True)
  all_day = models.IntegerField()
  calendar = models.DateTimeField()
  classification = models.CharField()
  create_date = models.DateTimeField()
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
  write_date = models.DateTimeField()
  write_uid = models.DateTimeField()
  
class calendar_event-calendar_category(models.Model):
  id = models.IntegerField(primary_key=True)
  category = models.CharField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  event = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.DateTimeField()
  
class calendar_event_alarm(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  event = models.CharField()
  valarm = model.CharField()
  write_date = models.DateTimeField()
  write_uid = models.DateTimeField()

class calendar_event_attendee(models.Model):  
  id = models.IntegerField(primary_key=True)
  attendee = models.CharField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  email = models.CharField()
  event = models.CharField()
  status = models.BooleanField()
  write_date = models.DateTimeField()
  write_uid = models.DateTimeField()
  
class calendar_event_exdate(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  date = models.DateTimeField()
  date_time = models.DateTimeField()
  event = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.DateTimeField()
  
class calendar_event_exrule(models.Model):
  id = models.IntegerField(primary_key=True)
  byday = models.IntegerField()
  byhour = models.IntegerField()
  byminute = models.IntegerField()
  bymonth = models.IntegerField()
  bymonthday = models.IntegerField()
  bysecond = models.IntegerField()
  bysetpos = models.IntegerField()
  byweekno = models.IntegerField()
  byyearday = models.IntegerField()
  count = models.IntegerField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  event = models.CharField()
  freq = models.IntegerField()
  interval = models.IntegerField()
  until = models.CharField()
  until_date = models.DateTimeField()
  wkst = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class calendar_event_rdate(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  date = models.DateTimeField()
  date_time = models.DateTimeField()
  event = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.DateTimeField()
  
class calendar_event_rrule(models.Model):
  id = models.IntegerField(primary_key=True)
  byday = models.IntegerField()
  byhour = models.IntegerField()
  byminute = models.IntegerField()
  bymonth = models.IntegerField()
  bymonthday = models.IntegerField()
  bysecond = models.IntegerField()
  bysetpos = models.IntegerField()
  byweekno = models.IntegerField()
  byyearday = models.IntegerField()
  count = models.IntegerField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  event = models.CharField()
  freq = models.IntegerField()
  interval = models.IntegerField()
  until = models.CharField()
  until_date = models.DateTimeField()
  wkst = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class calendar_location(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  name = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.DateTimeField()

class Meta:
    db_table = 'calendar_calendar'
    db_table = 'calendar_calendar-read-res_user'
    db_table = 'calendar_calendar-write-res_user'
    db_table = 'calender_category'
    db_table = 'calendar_event'
    db_table = 'calendar_event-calendar_category'
    db_table = 'calendar_event_alarm'
    db_table = 'calendar_event_attendee'
    db_table = 'calendar_event_exdate'
    db_table = 'calendar_event_exrule'
    db_table = 'calendar_event_rdate'
    db_table = 'calendar_event_rrule'
    db_table = 'calendar_location'