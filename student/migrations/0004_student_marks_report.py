# Generated by Django 3.1.2 on 2020-12-22 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20201222_1634'),
        ('student', '0003_student_roll_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks_report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.marksreport'),
        ),
    ]
