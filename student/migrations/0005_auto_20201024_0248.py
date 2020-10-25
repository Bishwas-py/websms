# Generated by Django 3.1.2 on 2020-10-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20201024_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='ethnicity',
            field=models.CharField(choices=[('brah', 'Brahmin'), ('cht', 'Chhetri'), ('jj', 'Janajati'), ('dl', 'Dalit'), ('md', 'Madhesi')], default='1', max_length=9),
        ),
    ]