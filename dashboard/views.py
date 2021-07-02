from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def dashboard(request):
	return render(request, 'index.html')

def register(request):
	form = UserCreationForm()
	context = {'form':form}

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/retirees')

	return render(request, 'register.html', context)

def login(request):
	return render(request, 'login.html')
