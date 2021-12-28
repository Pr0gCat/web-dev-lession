from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm, InfoUpdateForm
from . import models

def index(request):
    """
        Guide user to landing page
    """
    if request.user.is_authenticated:
        current_user =  models.User.objects.filter(user_entity=request.user).first()
        return render(request, 'landing.html', {"current_user": current_user})
    return render(request, 'landing.html')

def user_login(request):
    """
        Guide user to login page
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, 'registration/login.html', {'form': form, 'error': 'User does not exist'})
            login(request, authenticate(username=form.cleaned_data['username'], \
                password=form.cleaned_data['password']))
            return redirect(request.POST.get('next', '/'))
    form = LoginForm()
    return render(request, 'registration/login.html', 
        {
            'form': form,
            'next': request.GET.get('next', '/')
        })

def register(request):
    """
        Guide user to register page
    """
    error = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
                if User.objects.filter(username=form.cleaned_data['username']).exists():
                    error = '用户已存在'
                elif not str.isdigit(form.cleaned_data['contact_number']):
                    error = '請輸入正確的電話號碼'
                else:
                    user = User.objects.create_user(form.cleaned_data['username'], \
                        '', form.cleaned_data['password'])
                    user.save()
                    models.User.objects.create(user_entity=user, display_name=form.cleaned_data['display_name'], contact=form.cleaned_data['contact_number']).save()
                    login(request, user)
                    print('User created')
                    return redirect(request.POST.get('next', '/'))
            else:
                error = '密碼不一致'
        else:
            error = '帳號資訊錯誤'
    # Display a blank registration form.
    form = RegisterForm()
    return render(request, 'registration/register.html', {
        'form': form, 
        'error': error,
        'next': request.GET.get('next', '/')
    })

@login_required
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

@login_required
def s(request):
    """
        Guide user to shop mainpage
    """
    return render(request, 'shop/index.html')

@login_required
def user_profile(request, user_name):
    """
        Guide user to their profile
        User cannot access others address and contact
    """

    if request.method == 'POST':
        form = InfoUpdateForm(request.POST)
        user = models.User.objects.filter(user_entity=request.user).first()
        error = '輸入資訊錯誤'
        if form.is_valid():
            print(form.cleaned_data)
            if not str.isdigit(form.cleaned_data['contact']):
                return render(request, 'user_profile.html', {'tako_user': user, 'is_self': True, 'error': '請輸入正確的電話號碼'})
            if not form.cleaned_data['display_name']:
                return render(request, 'user_profile.html', {'tako_user': user, 'is_self': True, 'error': '顯示名稱不能為空'})
            if not form.cleaned_data['address']:
                return render(request, 'user_profile.html', {'tako_user': user, 'is_self': True, 'error': '請輸入地址'})
            
            user.display_name = form.cleaned_data['display_name']
            user.contact = form.cleaned_data['contact']
            user.address = form.cleaned_data['address']
            user.save()
            return render(request, 'user_profile.html', {'tako_user': user, 'is_self': True, 'msg': '更新成功'})
        return render(request, 'user_profile.html', {'tako_user': user, 'is_self': True, 'error': error})
    """
        GET
    """
    res = User.objects.filter(username=user_name)
    user = models.User.objects.filter(user_entity=request.user).first()
    # check if user exists
    if not res.exists():
        return render(request, 'user_profile.html', {'tako_user': user, 'is_self': True, 'error': f'找不到使用者 {user_name}!'})
    res = res.first()
    if res.username == 'admin':
        return render(request, 'user_profile.html', {'tako_user': user, 'is_self': True})
    # check if user is going to their profile
    if request.user.username == user_name:
        return render(request, 'user_profile.html', {"tako_user": user, 'is_self': True})
    else:
        # others profile
        other_user = User.objects.filter(username=user_name).first()
        others = models.User.objects.filter(user_entity=other_user).first()
        return render(request, 'user_profile.html', {"tako_user": others, 'is_self': False})

@login_required
def shop_profile(request, shop_name):
    """
        Guide user to shop info page
    """
    # check if user is going to their profile
    return render(request, 'profile.html')