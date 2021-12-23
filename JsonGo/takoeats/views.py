from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index(request):
    """
        Guide user to landing page
    """
    return render(request, 'landing.html')

def register(request):
    """
        Guide user to register page
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    # Display a blank registration form.
    form = UserCreationForm()
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