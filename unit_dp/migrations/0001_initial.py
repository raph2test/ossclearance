# Generated by Django 3.1.1 on 2021-06-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(choices=[('GENERAL', 'GENERAL'), ('LTGEN', 'LTGEN'), ('MGEN', 'MGEN'), ('BGEN', 'BGEN'), ('COL', 'COL'), ('LTC', 'LTC'), ('MAJ', 'MAJ'), ('CPT', 'CPT'), ('1LT', '1LT'), ('2LT', '2LT'), ('CMSGT', 'CMSGT'), ('SMSGT', 'SMSGT'), ('MSGT', 'MSGT'), ('TSGT', 'TSGT'), ('SSGT', 'SSGT'), ('SGT', 'SGT'), ('A1C', 'A1C'), ('AW1C', 'AW1C'), ('A2C', 'A2C'), ('AW2C', 'AW2C'), ('AM', 'AM'), ('AW', 'AW'), ('P2LT', 'P2LT')], max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('afsn', models.CharField(max_length=50, null=True)),
                ('bos', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
