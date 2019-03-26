from django.db import models

# Create your models here.
class product_category(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    name = models.CharField()
    parent = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    account_parent = models.BooleanField()
    accounting = models.BooleanField()
    taxes_parent = models.BooleanField()
    
class product_category_account(models.Model):
    id = models.IntegerField(primary_key=True)
    account_expense = models.IntegerField()
    account_revenue = models.IntegerField()
    category = models.IntegerField()
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_category_customer_taxes_rel(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    tax = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_category_supplier_taxes_rel(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    tax = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_configuration(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    default_accounts_category = models.BooleanField()
    default_taxes_category = models.BooleanField()
    
class product_configuration_default_cost_price_method(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    default_cost_price_method = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_cost_price(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    cost_price = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    product = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_cost_price_method(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    cost_price_method = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    template = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_customer_taxes_rel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    product = models.IntegerField()
    tax = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_list_price(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    list_price = models.IntegerField()
    template = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class product_product(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    code = models.CharField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    description = models.TextField()
    template = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    is_bed = models.BooleanField()
    is_insurance_plan = models.BooleanField()
    is_medical_supply = models.BooleanField()
    is_medicament = models.BooleanField()
    is_vaccine = models.BooleanField()
    is_prothesis = models.BooleanField()
    
class product_supplier_taxes_rel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    product = models.IntegerField()
    tax = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_template(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    consumable = models.BooleanField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    default_uom = models.IntegerField()
    name = models.CharField()
    type = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    account_category = models.IntegerField()
    accounts_category = models.BooleanField()
    taxes_category = models.BooleanField()
    purchaseable = models.BooleanField()
    purchase_uom = models.IntegerField()
    
class product_template-product_category(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    template = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()

class product_template-stock_lot_type(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    template = models.IntegerField()
    type = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_template_account(models.Model):
    id = models.IntegerField(primary_key=True)
    account_expense = models.IntegerField()
    account_revenue = models.IntegerField()
    company = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    template = models.IntegerField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_uom(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    category = models.IntegerField()
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    digits = models.IntegerField()
    factor = models.IntegerField()
    name = models.CharField()
    rate = models.IntegerField()
    rounding = models.IntegerField()
    symbol = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class product_uom_category(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(max_length=6)
    create_uid = models.IntegerField()
    name = models.CharField()
    write_date = models.DateTimeField(max_length=6)
    write_uid = models.IntegerField()
    
class Meta:
    db_table = 'product_category'
    db_table = 'product_category_account'
    db_table = 'product_category_customer_taxes_rel'
    db_table = 'product_category_supplier_taxes_rel'
    db_table = 'product_configuration'
    db_table = 'product_cost_price'
    db_table = 'product_cost_price_method'
    db_table = 'product_customer_taxes_rel'
    db_table = 'product_list_price'
    db_table = 'product_product'
    db_table = 'product_supplier_taxes_rel'
    db_table = 'product_template'
    db_table = 'product_template-product_category'
    db_table = 'product_template-stock_lot_type'
    db_table = 'product_template_account'
    db_table = 'product_uom'
    db_table = 'product_uom_category'