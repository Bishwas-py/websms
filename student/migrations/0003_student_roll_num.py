# Generated by Django 3.1.2 on 2020-12-22 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_roll_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
