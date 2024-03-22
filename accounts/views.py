from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import MyUserCreationForm

def signupaccount(request):
    #return render(request, 'signupaccount.html', {'form': UserCreationForm})
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': MyUserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password = request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('vspHome')
            except IntegrityError:
                return render(request, 'signupaccount.html', {
                    'form': MyUserCreationForm,
                    'error': 'This username has already been taken. Choose new username.',
                })
        else:
            return render(request, 'signupaccount.html', {
                'form': MyUserCreationForm, 
                'error': 'Your stupid Passwords do not match',
            })

@login_required
def logoutaccount(request):
    logout(request)
    return redirect('vspHome')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, 
            username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {
                'form': AuthenticationForm(),
                'error': 'username and password do not match',
            })
        else:
            login(request, user)
            return redirect('vspHome')