from django.forms import ModelForm
from .models import Personnel, Retirees, Unit_Requirements
from django.forms.widgets import DateInput, Select

class PersonnelForm(ModelForm):
	class Meta:
		model = Personnel
		fields = '__all__'

class RetireeForm(ModelForm):
	class Meta:
		model = Retirees
		fields = '__all__'
		exclude = ['created_by']

		widgets = {
			'date_applied' : DateInput(attrs={'type': 'date'}),
			'effectivity_date' : DateInput(attrs={'type': 'date'}),
			'assign_ghq' : Select(choices=[
				(True, 'Yes'),
				(False, 'No'),
			]),
		}

class UnitRequirementsForm(ModelForm):
	class Meta:
		model = Unit_Requirements
		fields = '__all__'
		exclude = ['ret_id']

		widgets = {
			'accountability' : Select(choices=[
				(True, 'Yes'),
				(False, 'No'),
			]),
			'unit_status' : Select(choices=[
				(True, 'Yes'),
				(False, 'No'),
			]),
		}