# Generated by Django 3.1.2 on 2020-10-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201021_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_details',
            name='nepali_established_date',
            field=models.CharField(default='2077-07-07', max_length=95),
        ),
    ]