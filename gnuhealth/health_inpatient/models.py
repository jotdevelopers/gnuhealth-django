from django.db import models


# Create your models here.

class gnuhealth_inpatient_diet(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    diet = models.IntegerField()
    name = models.IntegerField()
    remarks = models.TextField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_inpatient_icu(models.Model):
    id = models.IntegerField(primary_key=True)
    admitted = models.BooleanField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    discharged_from_icu = models.BooleanField()
    icu_admission_date = models.DateTimeField()
    icu_discharge_date = models.DateTimeField()
    name = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_inpatient_meal(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    diet_belief = models.IntegerField()
    diet_therapeutic = models.IntegerField()
    diet_vegetarian = models.IntegerField()
    institution = models.IntegerField()
    name = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_inpatient_meal_order(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    health_professional = models.IntegerField()
    meal_order = models.CharField(max_length=100)
    meal_warning = models.BooleanField()
    meal_warning_ack = models.BooleanField()
    mealtime = models.CharField(max_length=100)
    name = models.IntegerField()
    order_date = models.DateTimeField()
    remarks = models.TextField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_inpatient_meal_order_item(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    meal = models.IntegerField()
    name = models.IntegerField()
    remarks = models.TextField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_inpatient_medication(models.Model):
    id = models.IntegerField(primary_key=True)
    adverse_reaction = models.TextField()
    commom_dosage = models.IntegerField()
    course_completed = models.BooleanField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    discontinued = models.BooleanField()
    discontinued_reason = models.CharField(max_length=100)
    dose = models.IntegerField()
    dose_unit = models.IntegerField()
    end_treatment = models.DateTimeField()
    form = models.IntegerField()
    frequency = models.IntegerField()
    frequency_prn = models.BooleanField()
    frequency_unit = models.CharField(max_length=100)
    indication = models.IntegerField()
    is_active = models.BooleanField()
    medicament = models.IntegerField()
    name = models.IntegerField()
    qty = models.IntegerField()
    route = models.IntegerField()
    start_treatment = models.DateTimeField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_inpatient_medication_admin_time(models.Model):
    id = models.IntegerField(primary_key=True)
    admin_time = models.DateTimeField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    dose = models.IntegerField()
    dose_unit = models.IntegerField()    
    name = models.IntegerField()
    remarks = models.TextField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_inpatient_medication_log(models.Model):
    id = models.IntegerField(primary_key=True)
    admin_time = models.DateTimeField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    dose = models.IntegerField()
    dose_unit = models.IntegerField()
    health_professional = models.IntegerField()    
    name = models.IntegerField()
    remarks = models.TextField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    
class gnuhealth_inpatient_registration(models.Model):
    id = models.IntegerField(primary_key=True)
    admission_reason = models.IntegerField()
    admission_type = models.CharField(max_length=100)
    attending_physician = models.IntegerField()
    bed = models.IntegerField()
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    discharge_date = models.DateTimeField()
    discharge_dx = models.IntegerField()
    discharge_plan = models.TextField() 
    discharge_reason = models.CharField(max_length=100)
    discharged_by = models.IntegerField()
    hospitilization_date = models.DateTimeField()
    info = models.TextField()
    institution = models.IntegerField()   
    name = models.CharField(max_length=100)
    nursing_plan = models.TextField()
    nutrition_notes = models.TextField()
    operating_physician = models.IntegerField()
    patient = models.IntegerField()
    state = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    event = models.IntegerField()
    icu = models.BooleanField()
    
class Meta:
    db_table = 'gnuhealth_inpatient_diet'
    db_table = 'gnuhealth_inpatient_icu'
    db_table = 'gnuhealth_inpatient_meal'
    db_table = 'gnuhealth_inpatient_meal_order'
    db_table = 'gnuhealth_inpatient_meal_order_item'
    db_table = 'gnuhealth_inpatient_medication'
    db_table = 'gnuhealth_inpatient_medication_admin_time'
    db_table = 'gnuhealth_inpatient_medication_log'
    db_table = 'gnuhealth_inpatient_registration'
