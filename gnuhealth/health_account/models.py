from django.db import models
from django import db

# Create your models here.

class account_account(models.Model):
    id = models.IntegerField(primary_key=True)
    active = models.BooleanField(default=None)
    code = models.CharField(max_length=200)
    company = models.IntegerField()
    create_date = models.DateField()
    create_uid = models.IntegerField()
    deferral = models.BooleanField(default=None)
    general_ledger_balance = models.BooleanField(default=None)
    kind = models.CharField(max_length=200)
    left = models.IntegerField()
    name = models.CharField(max_length=200)
    note = models.CharField(max_length=200)
    parent = models.IntegerField()
    party_required = models.BooleanField(default=None)
    reconcile = models.BooleanField(default=None)
    right = models.IntegerField()
    second_currency = models.IntegerField()
    template = models.IntegerField()
    type = models.IntegerField()
    write_date = models.DateField()
    write_uid = models.IntegerField()


class account_account_deferral(models.Model):
    id = models.OneToOneField(AccountAccount.id)
    account = models.IntegerField()
    amount_second_currency = models.IntegerField()
    create_date = models.OneToOneField(AccountAccount.create_date)
    create_uid = models.OneToOneField(AccountAccount.create_uid)
    credit = models.IntegerField()
    debit = models.IntegerField()
    fiscal_year = models.IntegerField()
    write_date = models.OneToOneField(AccountAccount.write_date)
    write_uid = models.OneToOneField(AccountAccount.write_uid)


class account_account_tax_rel(models.Model):
    id = models.OneToOneField(AccountAccount.id)
    account = models.OneToOneField(AccountAccountDeferral.account)
    create_date = models.OneToOneField(AccountAccount.create_date)
    create_uid = models.OneToOneField(AccountAccount.create_uid)
    tax = models.IntegerField()
    write_date = models.OneToOneField(AccountAccount.write_date)
    write_uid = models.OneToOneField(AccountAccount.write_uid)


class account_account_template(models.Model):
    id = models.OneToOneField(AccountAccount.id)
    code = models.OneToOneField(AccountAccount.code)
    create_date = models.OneToOneField(AccountAccount.create_date)
    create_uid = models.OneToOneField(AccountAccount.create_uid)
    deferral = models.OneToOneField(AccountAccount.deferral)
    general_ledger_balance = models.OneToOneField(AccountAccount.general_ledger_balance)
    kind = models.OneToOneField(AccountAccount.kind)
    name = models.OneToOneField(AccountAccount.name)
    parent = models.OneToOneField(AccountAccount.parent)
    party_required = models.OneToOneField(AccountAccount.party_required)
    reconcile = models.OneToOneField(AccountAccount.reconcile)
    type = models.OneToOneField(AccountAccount.type)
    write_date = models.OneToOneField(AccountAccount.write_date)
    write_uid = models.OneToOneField(AccountAccount.write_uid)


class account_account_template_tax_rel (models.Model):
    id = models.OneToOneField(AccountAccountTemplate.id)
    account = models.IntegerField()
    create_date = models.OneToOneField(AccountAccountTemplate.create_date)
    create_uid = models.OneToOneField(AccountAccountTemplate.create_uid)
    tax = models.IntegerField()
    write_date = models.OneToOneField(AccountAccountTemplate.write_date)
    write_uid = models.OneToOneField(AccountAccountTemplate.write_uid)


class account_account_type (models.Model):
    id = models.OneToOneField(AccountAccount.id)
    balance_sheet = models.BooleanField(default=None)
    company = models.OneToOneField(AccountAccount.company)
    create_date = models.OneToOneField(AccountAccount.create_date)
    create_uid = models.OneToOneField(AccountAccount.create_uid)
    display_balance = models.IntegerField()
    income_statement = models.BooleanField(default=None)
    name = models.OneToOneField(AccountAccount.name)
    parent = models.OneToOneField(AccountAccount.parent)
    sequence = models.IntegerField()
    template = models.OneToOneField(AccountAccount.template)
    write_date = models.OneToOneField(AccountAccount.write_date)
    write_uid = models.OneToOneField(AccountAccount.write_uid)


class account_account_type_template (models.Model):
    id = models.OneToOneField(AccountAccount.id)
    balance_sheet = models.OneToOneField(AccountAccountType.balance_sheet)
    create_date = models.OneToOneField(AccountAccount.create_date)
    create_uid = models.OneToOneField(AccountAccount.create_uid)
    display_balance = models.OneToOneField(AccountAccountType.display_balance)
    income_statement = models.OneToOneField(AccountAccountType.income_statement)
    name = models.OneToOneField(AccountAccount.name)
    parent = models.OneToOneField(AccountAccount.parent)
    sequence = models.OneToOneField(AccountAccountType.sequence)
    write_date = models.OneToOneField(AccountAccount.write_date)
    write_uid = models.OneToOneField(AccountAccount.write_uid)

class Meta:
    db_table = 'account_account'
    db_table = 'account_account_deferral'
    db_table = 'account_account_tax_rel'
    db_table = 'account_account_template'
    db_table = 'account_account_template_tax_rel'
    db_table = 'account_account_type'
    db_table = 'account_account_type_template'