# Generated by Django 3.1.2 on 2020-10-20 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20201019_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_details',
            name='nepali_established_date',
            field=models.CharField(default='2077-07-04', max_length=95),
        ),
    ]