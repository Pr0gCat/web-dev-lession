from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm
from . import models

def index(request):
    """
        Guide user to landing page
    """
    return render(request, 'landing.html')

def user_login(request):
    """
        Guide user to login page
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, authenticate(username=form.cleaned_data['username'], \
                password=form.cleaned_data['password']))
            return redirect(request.POST.get('next', '/'))
    form = LoginForm()
    return render(request, 'registration/login.html', 
        {
            'form': form
        })

def register(request):
    """
        Guide user to register page
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
                user = User.objects.create_user(form.cleaned_data['username'], \
                    '', form.cleaned_data['password'])
                user.save()
                models.User(user=user, display_name=form.cleaned_data['display_name'], contact=form.cleaned_data['contact_no']).save()
                login(request, form.user)
                print('User created')
                return redirect(request.POST.get('next', '/'))

    # Display a blank registration form.
    form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='/login')
def d(request):
    """
        Guide user to delivery mainpage
    """
    return render(request, 'delivery/index.html')

def c(request):
    """
        Guide user to customer mainpage
    """
    return render(request, 'customer/index.html')

@login_required(login_url='/login')
def s(request):
    """
        Guide user to shop mainpage
    """
    return render(request, 'shop/index.html')