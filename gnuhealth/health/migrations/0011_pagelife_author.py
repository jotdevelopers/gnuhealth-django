# Generated by Django 2.1.7 on 2019-08-29 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0010_auto_20190830_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelife',
            name='author',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
