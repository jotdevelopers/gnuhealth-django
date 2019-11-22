from django.db import models

# Create your models here.
class gnuhealth_ethnicity(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_ethnicity'
        
        
class gnuhealth_occupation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_occupation'

class gnuhealth_procedure(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_procedure'
        
class gnuhealth_specialty(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_specialty'

class gnuhealth_imaging_test_type(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_imaging_test_type'
        
class gnuhealth_hospital_building(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    institution = models.IntegerField()
    extra_info = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'gnuhealth_hospital_building'
        
class gnuhealth_hospital_unit(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    institution = models.IntegerField()
    extra_info = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'gnuhealth_hospital_unit'
        
class gnuhealth_imaging_test(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    active = models.BooleanField()
    code = models.CharField(max_length=100)
    product = models.IntegerField()
    test_type = models.IntegerField()
    class Meta:
        db_table = 'gnuhealth_imaging_test'


class gnuhealth_disease_genes(models.Model):
      id = models.IntegerField(primary_key=True)
      chromosome = models.CharField(max_length = 100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      gene_id = models.CharField(max_length = 100)
      info = models.CharField(max_length=100)
      location = models.CharField(max_length = 100)
      long_name = models.CharField(max_length = 100)
      name = models.CharField(max_length=100)
      protein_name = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
             db_table = 'gnuhealth_disease_gene'
             
class gnuhealth_gene_varient(models.Model):
      id = models.IntegerField(primary_key=True)
      aa_change = models.CharField(max_length = 100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      name = models.IntegerField()
      varient = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
             db_table = 'gnuhealth_gene_varient'

class gnuhealth_pathology_group(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    desc = models.CharField(max_length = 100)
    info = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
            db_table = 'gnuhealth_pathology_group'

class gnuhealth_pathology_category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_date = models.DateTimeField()
    write_uid = models.IntegerField()
    class Meta:
            db_table = 'gnuhealth_pathology_category'            

class gnuhealth_body_function(models.Model):
      id = models.IntegerField(primary_key=True)
      # category = models.IntegerField()
      code = models.CharField(max_length=100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      name = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
              db_table = 'gnuhealth_body_function'

class gnuhealth_body_structure(models.Model):
      id = models.IntegerField(primary_key=True)
      # category = models.IntegerField()
      code = models.CharField(max_length=100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      name = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
            db_table = 'gnuhealth_body_structure'

class gnuhealth_activity_and_participation(models.Model):
      id = models.IntegerField(primary_key=True)
      # category = models.IntegerField()
      code = models.CharField(max_length=100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      name = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
            db_table = 'gnuhealth_activity_and_participation'

class gnuhealth_environmental_factor(models.Model):
      id = models.IntegerField(primary_key=True)
      # category = models.IntegerField()
      code = models.CharField(max_length=100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      name = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
            db_table = 'gnuhealth_environmental_factor'

class gnuhealth_diet_belief(models.Model):
      id = models.IntegerField(primary_key=True)
      code = models.CharField(max_length=100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      description = models.CharField(max_length=100)
      name = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
            db_table = 'gnuhealth_diet_belief'

class gnuhealth_diet_therapeutic(models.Model):
      id = models.IntegerField(primary_key=True)
      code = models.CharField(max_length=100)
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()
      description = models.CharField(max_length=100)
      name = models.CharField(max_length=100)
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
            db_table = 'gnuhealth_diet_therapeutic'

class gnuhealth_pediatrics_growth_charts_who(models.Model):
      id = models.IntegerField(primary_key=True)
      indicator = models.CharField(max_length=100)
      measure = models.CharField(max_length=100)
      month = models.IntegerField()
      sex = models.CharField(max_length=10)
      type = models.CharField(max_length=100)
      value = models.FloatField()
      create_date = models.DateTimeField()
      create_uid = models.IntegerField()      
      write_date = models.DateTimeField()
      write_uid = models.IntegerField()
      class Meta:
            db_table = 'gnuhealth_pediatrics_growth_charts_who'
            
class gnuhealth_operational_sector(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    info = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    operational_area = models.IntegerField()
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

class gnuhealth_family(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_family'
    
class gnuhealth_family_member(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.IntegerField()
    write_uid = models.IntegerField()
    name = models.IntegerField()
    party= models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    class Meta:
        db_table = 'gnuhealth_family_member'
        