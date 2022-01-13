from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


def register_account(request):
    if request.method == 'GET':
        return render(request, 'account/register_account.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('maketodo:currenttodo')
            except IntegrityError:
                return render(request, 'account/register_account.html',
                              {'form': UserCreationForm(), 'error': 'User already exists'})
        else:
            return render(request, 'account/register_account.html',
                          {'form': UserCreationForm(), 'error': 'Passwords mismatch'})



def login_account(request):
    if request.method == 'GET':
        return render(request, 'account/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'account/login.html',
                          {'form': AuthenticationForm(),
                           'error': 'User or password not defined. You must register'})
        else:
            login(request, user)
            return redirect('maketodo:currenttodo')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('maketodo:home')
