# Generated by Django 2.1.7 on 2019-08-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gnuhealth_gene_variant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('aa_change', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField()),
                ('create_uid', models.IntegerField()),
                ('name', models.IntegerField()),
                ('varient', models.CharField(max_length=100)),
                ('write_date', models.DateTimeField()),
                ('write_uid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='gnuhealth_gene_variant_phenotype',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField()),
                ('create_uid', models.IntegerField()),
                ('name', models.IntegerField()),
                ('phenotype', models.IntegerField()),
                ('varient', models.CharField(max_length=100)),
                ('write_date', models.DateTimeField()),
                ('write_uid', models.IntegerField()),
            ],
        ),
    ]
