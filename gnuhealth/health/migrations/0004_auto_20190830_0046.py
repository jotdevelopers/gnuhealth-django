# Generated by Django 2.1.7 on 2019-08-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_auto_20190830_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gnuhealth_pol',
            name='person',
            field=models.IntegerField(default=''),
        ),
    ]
