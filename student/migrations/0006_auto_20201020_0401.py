# Generated by Django 3.1.2 on 2020-10-20 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
        ('student', '0005_auto_20201016_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.student_class'),
        ),
    ]
