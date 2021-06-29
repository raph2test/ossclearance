# Generated by Django 3.1.1 on 2021-06-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_dp', '0007_auto_20210623_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit_requirements',
            name='uploaded_cmd_clearance',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='unit_requirements',
            name='uploaded_sos',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='unit_requirements',
            name='uploaded_unit_clearance',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='unit_requirements',
            name='accountability',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='unit_requirements',
            name='unit_status',
            field=models.BooleanField(default=0),
        ),
    ]
