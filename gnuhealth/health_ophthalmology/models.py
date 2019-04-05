from django.db import models

# Create your models here.

class gnuhealth_ophthalmology_findings(models.Model):
  id = models.IntegerField(primary_key=True)
  affected_eye = model.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  eye_structure = mdoels.CharField()
  finding = models.CharField()
  name = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_ophthalmology_evaluation(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateField()
  create_uid = models.IntegerField()
  health_professional = models.CharField()
  iop_method = models.CharField()
  laxis = models.CharField()
  lbcva = models.CharField()
  lbcva_axis = models.CharField()
  lbcva_cylinder = models.CharField()
  lbcva_nv = models.CharField()
  lbcva_nv_add = models.CharField()
  lbcva_spherical = models.CharField()
  lcylinder = models.CharField()
  ldva = models.CharField()
  ldva_aid = models.CharField()
  ldva_pinhole = models.CharField()
  liop = models.CharField()
  lnv = models.CharField()
  lnv_add = models.CharField()
  lspherical = models.CharField()
  
class Meta:
    db_table = 'gnuhealth_ophthalmology_findings'
    db_table = 'gnuhealth_ophthalmology_evaluation'