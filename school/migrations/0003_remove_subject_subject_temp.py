# Generated by Django 3.1.2 on 2020-12-21 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_subject_subject_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='subject_temp',
        ),
    ]