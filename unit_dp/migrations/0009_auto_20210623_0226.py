# Generated by Django 3.1.1 on 2021-06-22 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_dp', '0008_auto_20210623_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit_requirements',
            name='uploaded_cmd_clearance',
            field=models.FileField(blank=True, null=True, upload_to='cmd_clearance'),
        ),
        migrations.AlterField(
            model_name='unit_requirements',
            name='uploaded_sos',
            field=models.FileField(blank=True, null=True, upload_to='unit_sos'),
        ),
        migrations.AlterField(
            model_name='unit_requirements',
            name='uploaded_unit_clearance',
            field=models.FileField(blank=True, null=True, upload_to='unit_clerance'),
        ),
    ]
