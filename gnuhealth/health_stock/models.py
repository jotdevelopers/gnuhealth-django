from django.db import models

# Create your models here.

class stock_configuration(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class stock_configuration_location(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    shipment_internal_transit = models.IntegerField() 
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class stock_configuration_sequence(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    inventory_sequence = models.IntegerField()
    shipment_in_return_sequence = models.IntegerField()
    shipment_in_sequence = models.IntegerField()
    shipment_internal_sequence = models.IntegerField()
    shipment_out_return_sequence = models.IntegerField()
    shipment_out_sequence = models.IntegerField() 
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class stock_inventory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    date = models.DateField()
    location = models.IntegerField()
    lost_found = models.IntegerField()
    number = models.CharField()
    state = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class stock_inventory_line(models.Model):  
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    expected_quantity = models.FloatField()
    inventory = models.IntegerField()
    product = models.IntegerField()
    quantity = models.FloatField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    lot = models.ForeignKey(stock_lot)
    
class stock_location(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    address = models.IntegerField()
    code = models.CharField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    flat_childs = models.BooleanField()
    input_location = models.IntegerField()
    left = models.IntegerField()
    name = models.CharField()
    output_location = models.IntegerField()
    parent = models.IntegerField()
    picking_location = models.IntegerField()
    right = models.IntegerField()
    storage_location = models.IntegerField()
    type = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    supplier_return_location = models.IntegerField()
    overflowing_location = models.IntegerField()
    provisioning_location = models.IntegerField()

class stock_location_lead_time(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    lead_time = models.DurationField()
    sequence = models.IntegerField()
    warehouse_from = models.IntegerField()
    warehouse_to = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class stock_move(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    cost_price = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    currency =  models.IntegerField()
    effective_date = models.DateField()
    from_location = models.IntegerField()
    internal_quantity = models.FloatField()
    origin = models.CharField()
    planned_date = models.DateField()
    product = models.IntegerField()
    quantity = models.FloatField()
    shipment = models.CharField()
    state = models.CharField()
    to_location = models.IntegerField()
    unit_price = models.IntegerField()
    uom = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    lot = models.ForeignKey(stock_lot)

class stock_order_point(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    max_quantity = models.FloatField()
    min_quantity = models.FloatField()
    overflowing_location = models.IntegerField()
    product = models.IntegerField()
    provisioning_location = models.IntegerField()
    storage_location = models.IntegerField()
    target_quantity = models.FloatField()
    type = models.CharField()
    warehouse_location = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class stock_period(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    date = models.DateField()
    state = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class stock_period_cache(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    internal_quantity = models.FloatField()
    location = models.ForeignKey(stock_location)
    period = models.ForeignKey(stock_period)
    product = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class stock_period_cache_lot(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    internal_quantity = models.FloatField()
    location = models.ForeignKey(stock_location)
    lot = models.ForeignKey(stock_lot)
    period = models.ForeignKey(stock_period)
    product = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class stock_shipment_in(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    contact_address = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    done_by = models.IntegerField()
    effective_date = models.DateField()
    number = models.CharField()
    planned_date = models.DateField()
    recieved_by = models.IntegerField()
    reference = models.CharField()
    state = models.CharField()
    supplier = models.IntegerField()
    warehouse = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class stock_shipment_in_return(models.Model): 
    id = models.IntegerField(primary_key=True)
    assigned_by = models.IntegerField()
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    delivery_address = models.IntegerField()
    done_by = models.IntegerField()
    effective_date = models.DateField()
    from_location = models.IntegerField()
    number = models.CharField()
    planned_date = models.DateField()
    reference = models.CharField()
    state = models.CharField()
    supplier = models.IntegerField()
    to_location = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class stock_shipment_internal(models.Model):
    id = models.IntegerField(primary_key=True)
    assigned_by = models.IntegerField()
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    done_by = models.IntegerField()
    effective_date = models.DateField()
    effective_start_date = models.DateField()
    from_location = models.IntegerField()
    number = models.CharField()
    planned_date = models.DateField()
    planned_start_date = models.DateField()
    reference = models.CharField()
    shipped_by = models.IntegerField()
    state = models.CharField()
    to_location = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class stock_shipment_out(models.Model):
    id = models.IntegerField(primary_key=True)
    assigned_by = models.IntegerField()
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    customer = models.IntegerField()
    delivery_address = models.IntegerField()
    done_by = models.IntegerField()
    effective_date = models.DateField()
    number = models.CharField()
    packed_by = models.IntegerField()
    planned_date = models.DateField()
    reference = models.CharField()
    state = models.CharField()
    warehouse = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class stock_shipment_out_return(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField() 
    customer = models.IntegerField()
    delivery_address = models.IntegerField()
    done_by = models.IntegerField()
    effective_date = models.DateField()
    number = models.CharField()
    planned_date = models.DateField()
    recieved_by = models.IntegerField()
    reference = models.CharField()
    state = models.CharField()
    warehouse = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class Meta:
    db_table = 'stock_configuration'
    db_table = 'stock_configuration_location'
    db_table = 'stock_configuration_sequence'
    db_table = 'stock_inventory'
    db_table = 'stock_inventory_line'
    db_table = 'stock_location'
    db_table = 'stock_location_lead_time'
    db_table = 'stock_move'
    db_table = 'stock_order_point'
    db_table = 'stock_period'
    db_table = 'stock_period_cache'
    db_table = 'stock_period_cache_lot'
    db_table = 'stock_shipment_in'
    db_table = 'stock_shipment_in_return'
    db_table = 'stock_shipment_internal'
    db_table = 'stock_shipment_out'
    db_table = 'stock_shipment_out_return'