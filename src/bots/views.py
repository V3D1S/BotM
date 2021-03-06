from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .forms import UploadBotForm
from .models import Bot


# Handling functions 

	




# Create your views here.
def homeView(request):
	bots = Bot.objects.all()
	all_bots = []
	for bot in bots:
		bot_info = {"title": bot.title, "description": bot.description, "price": bot.price, "author": bot.author, "id": id}
		all_bots.append(bot_info)

	return render(request, 'bots/index.html', {'bots': bots})
    

def logout(request):
	do_logout(request)
	return redirect('/')
	


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
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			do_login(request, user)
			return redirect('/')
	else: 
		form = UserCreationForm()

	return render(request, 'bots/sign_up.html', {'form': form})


def upload_bot(request):
	if request.method == "POST":
		form = UploadBotForm(request.POST, request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			price = form.cleaned_data['price']
			file = request.FILES['file']
			bot = Bot(title=title, description=description, price=price, author=request.user.username, file=file)
			bot.save()
			return redirect('/')
	else:
		form = UploadBotForm()

	return render(request, 'bots/upload.html', {'form': form})


def bot_details(request, pk):
	bot = Bot.objects.get(id=pk)
	return render(request, 'bots/bot_details.html', {"bot": bot})


def bot_page(request):
	bots = Bot.objects.all()


	return render(request, 'bots/bots.html', {"bots": bots})


def profile(request):
	if request.user.is_authenticated:
		username = request.user.username
		password = request.user.password

		print(username, password)

		return redirect('/')