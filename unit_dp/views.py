from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import PersonnelForm, RetireeForm, UnitRequirementsForm

# Create your views here.

def index(request):
	personnel = Personnel.objects.all()

	total_personnel = personnel.count()

	context = {'personnel':personnel}
	return render(request, 'unit_dp/index.html', context)

def personnel(request, pk):
	personnel = Personnel.objects.get(id=pk)
	context = {'personnel':personnel}
	return render(request, 'unit_dp/personnel.html', context)

def addPersonnel(request):
	# action = 'create'
	form = PersonnelForm()
	if request.method == 'POST':
		form = PersonnelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/unit-dp')

	context =  {'form':form}
	return render(request, 'unit_dp/personnel_form.html', context)

def retirees(request):
	retirees = Retirees.objects.all()

	total_retirees = retirees.count()
	context = {'retirees':retirees, 'total_retirees':total_retirees}
	return render(request, 'unit_dp/retirees.html', context)

def retireeView(request, pk):
	retiree = Retirees.objects.get(id=pk)
	form = UnitRequirementsForm()
	retiree_request = Unit_Requirements.objects.filter(ret_id=retiree.id)
	if request.method == 'POST':
		form = UnitRequirementsForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.ret_id_id = retiree.id
			instance.purpose = instance.purpose
			instance.accountability = instance.accountability
			instance.uploaded_sos = instance.uploaded_sos
			instance.uploaded_cmd_clearance = instance.uploaded_cmd_clearance
			instance.uploaded_unit_clearance = instance.uploaded_unit_clearance
			instance.unit_status = instance.unit_status
			instance.save()
			return redirect('/retirees')
	context = {'form':form, 'retiree':retiree, 'retiree_req':retiree_request}
	return render(request, 'unit_dp/retiree_view.html', context)

def addRetiree(request):
	# action = 'create'
	form = RetireeForm()
	# print(form)
	# print(form['pers_id'])
	form['pers_id'].label = 'Personnel'
	if request.method == 'POST':
		form = RetireeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/retirees')

	context =  {'form':form}
	return render(request, 'unit_dp/retiree_form.html', context)

def deleteRetiree(request, pk):
	retiree = Retirees.objects.get(id=pk)
	if request.method == 'POST':
		retiree.delete()
		return redirect('/retirees')
	
	context =  {}	
	return render(request, 'unit_dp/retiree_view.html', context)