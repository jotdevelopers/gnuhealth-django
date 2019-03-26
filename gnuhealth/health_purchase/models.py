from django.db import models

# Create your models here.

class purchase_configuration(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class purchase_configuration_purchase_method(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    purchase_invoice_method = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class purchase_configuration_sequence(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    purchase_sequence = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class purchase_configuration_supply_period(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    supply_period = models.DurationField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class purchase_invoice_ignored_rel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    invoice = models.IntegerField()
    purchase = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class purchase_invoice_recreated_rel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    invoice = models.IntegerField()
    purchase = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class purchase_line(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    delivery_date_edit = models.BooleanField()
    delivery_date_stored = models.DateField()
    description = models.TextField()
    note = models.TextField()
    product = models.IntegerField()
    purchase = models.IntegerField()
    quantity = models.IntegerField()
    sequence = models.IntegerField()
    type = models.CharField()
    unit = models.IntegerField()
    unit_price = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class purchase_line_account_tax(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    line = models.IntegerField()
    tax = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class purchase_line_moves_ignored_rel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    move = models.IntegerField()
    purchase_line = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class purchase_line_moves_recreated_rel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    move = models.IntegerField()
    purchase_line = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class purchase_product_supplier(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField()
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    currency = models.IntegerField()
    lead_time = models.DurationField()
    name = models.CharField()
    party = models.IntegerField()
    product = models.IntegerField()
    sequence = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class purchase_product_supplier_price(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    product_supplier = models.IntegerField()
    lead_time = models.DurationField()
    quantity = models.IntegerField()
    sequence = models.IntegerField()
    unit_price = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class purchase_purchase(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField()
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    currency = models.IntegerField()
    deliver_date = models.DateField()
    description = models.CharField()
    invoice_address = models.IntegerField()
    invoice_method = models.CharField()
    invoice_state = models.CharField()
    number = models.CharField()
    party = models.IntegerField()
    payment_term = models.IntegerField()
    purchase = models.DateField()
    reference = models.CharField()
    shipment_state = models.CharField()
    state = models.CharField()
    tax_amount_cache = models.IntegerField()
    total_amount_chache = models.IntegerField()
    untaxed_amount_cache = models.IntegerField()
    warehouse = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
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
    db_table = 'purchase_configuration'
    db_table = 'purchase_configuration_purchase_method'
    db_table = 'purchase_configuration_sequence'
    db_table = 'purchase_configuration_supply_period'
    db_table = 'purchase_invoice_ignored_rel'
    db_table = 'purchase_invoice_recreated_rel'
    db_table = 'purchase_line'
    db_table = 'purchase_line_account_tax'
    db_table = 'purchase_line_moves_ignored_rel'
    db_table = 'purchase_line_moves_recreated_rel'
    db_table = 'purchase_product_supplier'
    db_table = 'purchase_product_supplier_price'
    db_table = 'purchase_purchase'
    db_table = 'purchase_request'