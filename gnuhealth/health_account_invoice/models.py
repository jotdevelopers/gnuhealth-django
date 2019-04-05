from django.db import models

# Create your models here.

class account_invoice(models.Model):
  id = models.IntegerField(primary_key=True)
  account = models.CharField()
  accounting_date = models.DateTimeField()
  cancel_move = models.DateTimeField()
  create_uid = models.IntegerField()
  currency = models.IntegerField()
  description = models.CharField()
  invoice_address = models.CharField()
  invoice_date = models.DateTimeField()
  invoice_report_cache = models.CharField()
  invoice_report_cache_id = models.IntegerField()
  invoice_report_format = models.CharField()
  journal = models.CharField()
  move = models.CharField()
  number = models.IntegerField()
  party = models.CharField()
  party_tax_identifier = models.CharField()
  payment_term = models.CharField()
  reference = models.CharField()
  state = models.CharField()
  tax_identifier = models.CharField()
  type = models.CharField()
  write_date = models.DateTmeField()
  write_uid = models.IntegerField()
  
class account_invoice-account_move_line(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  invoice = models.IntegerField()
  line = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class account_invoice_line(models.Model):
  id = models.IntegerField(primary_key=True)
  account = models.CharField()
  company = models.CharField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  currency = models.IntegerField()
  description = models.CharField()
  invoice = models.IntegerField()
  invoice_type = models.CharField()
  note = models.CharField()
  origin = models.CharField()
  party = models.CharField()
  product = models.CharField()
  quantity = models.IntegerField()
  sequence = models.CharField()
  type = models.CharField()
  unit = models.CharField()
  unit_price = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class account_invoice_line-stock_move(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  invoice_line = models.CharField()
  stock_move = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class account_invoice_line_account_tax(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  line = models.CharField()
  tax = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class account_invoice_payment_term(models.Model):
  id = models.IntegerField(primary_key=True)
  active = models.CharField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  description = models.CharField()
  name = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class account_invoice_payment_term_line(models.Model):
  id = models.IntegerField(primary_key=True)
  amount = models.IntegerField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  currency = models.IntegerField()
  divisor = models.IntegerField()
  payment = models.IntegerField()
  ratio = models.IntegerField()
  sequence = models.CharField()
  type = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
  
class account_invoice_payment_term_line_delta(models.Model):
  id = models.IntegerField(primary_key=True)
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  day = models.IntegerField()
  days = models.IntegerField()
  line = models.CharField()
  month = models.IntegerField()
  months = models.IntegerField()
  sequence = models.CharField()
  weekday = models.BooleanField()
  weeks = models.IntegerField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class account_invoice_tax(models.Model):
  id = models.IntegerField(primary_key=True)
  account = models.CharField()
  amount = models.IntegerField()
  base = models.CharField()
  base_code = models.IntegerField()
  base_sign = models.CharField()
  create_date = models.DateTimeField()
  create_uid = models.IntegerField()
  description = models.CharField()
  invoice = models.IntegerField()
  legal_notice = models.CharField()
  manual = models.CharField()
  sequence = models.CharField()
  tax = models.IntegerField()
  tax_code = models.IntegerField()
  tax_sign = models.CharField()
  write_date = models.DateTimeField()
  write_uid = models.IntegerField()
  
class Meta:
    db_table = 'account_invoice'
    db_table = 'account_invoice-account_move_line'
    db_table = 'account_invoice_line'
    db_table = 'account_invoice_line-stock_move'
    db_table = 'account_invoice_line_account_tax'
    db_table = 'account_invoice_payment_term'
    db_table = 'account_invoice_payment_term_line'
    db_table = 'account_invoice_payment_term_line_delta'
    db_table = 'account_invoice_tax'
  
  
  
