from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

# Create your views here.
def homeView(request):
	return render(request, 'bots/index.html')
    

def logout(request):
	do_logout(request)
	return render(request, 'bots/index.html')
	


def sign_in(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)

			if user is not None: 
				do_login(request, user)

				return redirect('/')
				
	context = {'form': form}

	return render(request, 'bots/sign_in.html', context)


def sign_up(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			do_login(request, user)
			return redirect('/')
	else: 
		form = UserCreationForm()

	return render(request, 'bots/sign_up.html', {'form': form})
