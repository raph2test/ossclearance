# Generated by Django 3.1.1 on 2021-06-22 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit_dp', '0006_auto_20210623_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit_requirements',
            name='uploaded_cmd_clearance',
        ),
        migrations.RemoveField(
            model_name='unit_requirements',
            name='uploaded_sos',
        ),
        migrations.RemoveField(
            model_name='unit_requirements',
            name='uploaded_unit_clearance',
        ),
    ]