from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .filters import UserFilter


def home(request):
	return render(request, 'home.html')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid:
			form.save()
			return 	redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form':form})

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})
