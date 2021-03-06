# Generated by Django 3.1.1 on 2021-06-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_dp', '0004_auto_20210622_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retirees',
            name='assign_ghq',
            field=models.CharField(choices=[(1, 'Yes'), (0, 'No')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='unit_requirements',
            name='accountability',
            field=models.CharField(choices=[(1, 'Yes'), (0, 'No')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='unit_requirements',
            name='unit_status',
            field=models.CharField(choices=[(1, 'Yes'), (0, 'No')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='unit_requirements',
            name='uploaded_sos',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
