# Generated by Django 3.1.2 on 2020-12-22 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_marksreport_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marksreport',
            name='school',
        ),
        migrations.RemoveField(
            model_name='marksreport',
            name='student',
        ),
    ]