from django.db import models
import datetime

# Create your models here.

class Personnel(models.Model):

	RANK = (
		('GENERAL', 'GENERAL'),
		('LTGEN', 'LTGEN'),
		('MGEN', 'MGEN'),
		('BGEN', 'BGEN'),
		('COL', 'COL'),
		('LTC', 'LTC'),
		('MAJ', 'MAJ'),
		('CPT', 'CPT'),
		('1LT', '1LT'),
		('2LT', '2LT'),
		('CMSGT', 'CMSGT'),
		('SMSGT', 'SMSGT'),
		('MSGT', 'MSGT'),
		('TSGT', 'TSGT'),
		('SSGT', 'SSGT'),
		('SGT', 'SGT'),
		('A1C', 'A1C'),
		('AW1C', 'AW1C'),
		('A2C', 'A2C'),
		('AW2C', 'AW2C'),
		('AM', 'AM'),
		('AW', 'AW'),
		('P2LT', 'P2LT'),
	)
	rank = models.CharField(max_length=200, null=True, choices=RANK)
	first_name = models.CharField(max_length=200, null=True)
	middle_name = models.CharField(max_length=200, null=True)
	last_name = models.CharField(max_length=200, null=True)
	afsn = models.CharField(max_length=50, null=True)
	bos = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.first_name + " " + self.last_name



class Type_Of_Purpose(models.Model):
	type_of_purpose = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.type_of_purpose
	


class Retirees(models.Model):

	# ASSIGN_GHQ = (
	# 	(1, 'Yes'),
	# 	(0, 'No'),
	# )
	pers_id = models.ForeignKey(Personnel, on_delete= models.SET_NULL, null=True)
	purpose = models.ForeignKey(Type_Of_Purpose, on_delete= models.SET_NULL, null=True)
	date_applied = models.CharField(max_length=100, null=True)
	effectivity_date = models.CharField(max_length=100, null=True)
	assign_ghq = models.BooleanField( default=0)
	created_by = models.CharField(max_length=255, null=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.pers_id.first_name


class Unit_Requirements(models.Model):

	# ACCOUNTABILITY = (
	# 	(1, 'Yes'),
	# 	(0, 'No'),
	# )

	# UNIT_STATUS = (
	# 	(1, 'Yes'),
	# 	(0, 'No'),
	# )

	ret_id = models.ForeignKey(Retirees, on_delete= models.SET_NULL, null=True)
	uploaded_sos = models.FileField(null=True, blank=True, upload_to='unit_sos')
	uploaded_cmd_clearance = models.FileField(null=True, blank=True,upload_to='cmd_clearance')
	accountability = models.BooleanField( default=0)
	uploaded_unit_clearance = models.FileField(null=True, blank=True, upload_to='unit_clearance')
	unit_status = models.BooleanField( default=0)


