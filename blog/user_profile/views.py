from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.


def Register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = RegisterForm()
    return render(
        request,
        'user_profile/registration.html',
        {'user_form':user_form, 'registered':registered}
    )