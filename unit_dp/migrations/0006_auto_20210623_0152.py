# Generated by Django 3.1.1 on 2021-06-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_dp', '0005_auto_20210623_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit_requirements',
            name='uploaded_cmd_clearance',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='unit_requirements',
            name='uploaded_unit_clearance',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
