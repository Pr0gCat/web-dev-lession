from django.shortcuts import render

def index(request):
    """
        Guide user to landing page
    """
    return render(request, 'landing.html')

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

def s(request):
    """
        Guide user to shop mainpage
    """
    return render(request, 'shop/index.html')