# Generated by Django 2.1.7 on 2019-08-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gnuhealth_surgery',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('admission', models.IntegerField()),
                ('age', models.CharField(max_length=100)),
                ('anesthesia_report', models.TextField()),
                ('anesthetist', models.IntegerField()),
                ('classification', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('create_date', models.DateField()),
                ('create_uid', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('extra_info', models.TextField()),
                ('institution', models.IntegerField()),
                ('operating_room', models.IntegerField()),
                ('pathology', models.IntegerField()),
                ('patient', models.IntegerField()),
                ('postoperative_dx', models.IntegerField()),
                ('preop_antibiotics', models.BooleanField()),
                ('preop_asa', models.CharField(max_length=100)),
                ('preop_bleeding_risk', models.BooleanField()),
                ('preop_mallampati', models.CharField(max_length=100)),
                ('preop_oximeter', models.BooleanField()),
                ('preop_rcri', models.IntegerField()),
                ('preop_site_marking', models.BooleanField()),
                ('preop_sterility', models.BooleanField()),
                ('signed_by', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('surgeon', models.IntegerField()),
                ('surgery_date', models.DateField()),
                ('surgery_end_date', models.DateField()),
                ('surgical_wound', models.CharField(max_length=100)),
                ('write_date', models.DateField()),
                ('write_uid', models.IntegerField()),
                ('main_procedure', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='gnuhealth_surgery_supply',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('create_date', models.DateField()),
                ('create_uid', models.IntegerField()),
                ('name', models.IntegerField()),
                ('notes', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('qty_used', models.IntegerField()),
                ('supply', models.IntegerField()),
                ('write_date', models.DateField()),
                ('write_uid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='gnuhealth_surgery_team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('create_date', models.DateField()),
                ('create_uid', models.IntegerField()),
                ('name', models.IntegerField()),
                ('notes', models.CharField(max_length=100)),
                ('roles', models.IntegerField()),
                ('team_member', models.IntegerField()),
                ('supply', models.IntegerField()),
                ('write_date', models.DateField()),
                ('write_uid', models.IntegerField()),
            ],
        ),
    ]
