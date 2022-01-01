from django.urls import path
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect

from .models import Shop, Item, ItemCategory
from .forms import AddItemForm

def get_random_opened_shop(request):
    pass

"""
商店管理
"""
@login_required
def toggle_shop(request):
    """
    """
    if request.method == 'POST' and request.is_ajax():
        shop_id = request.POST.get('shop_id')
        shop = Shop.objects.get(id=shop_id)
        if shop.owner != request.user:
            return JsonResponse({'status': 'faliure'})
        shop.opened = not shop.opened
        shop.save()
        return JsonResponse({'status': 'success'})
    elif request.method == 'GET':
        shop_id = request.GET.get('shop_id')
        shop = Shop.objects.get(id=shop_id)
        if shop != None:
            return JsonResponse({'status': 'success', 'opened': shop.opened})
    return JsonResponse({'status': 'faliure'})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            print(form)
            #no validation
            print(request.POST)
            shop = Shop.objects.get(owner=request.user)
            category = ItemCategory.objects.filter(shop=shop, name=request.POST.get('category'))
            if category.exists():
                category = category.first()
            else:
                category = ItemCategory.objects.create(shop=shop, name=request.POST.get('category'))
            
            Item.objects.create(shop=shop, \
                name=request.POST.get('name'), \
                price=request.POST.get('price'), \
                desc=request.POST.get('desc'),\
                status=(0 if request.POST.get('available') else 1),\
                category=category,
                image=request.FILES.get('image')
                            )
    return redirect('/s')

@login_required
def accept_order(request):
    pass

@login_required
def cancel_order(request):
    pass

"""
外送員
"""
@login_required
def get_available_order(request):
    pass

@login_required
def assign_order(request):
    pass

"""
訂單管理
"""
@login_required
def finish_order_task(request):
    """
        customer: 完成訂單
        shop: 訂單準備完成
        delivery: 訂單已送達
    """
    pass

@login_required
def get_order_status(request):
    pass


urlpatterns = [
    path('randshop', get_random_opened_shop, name='randshop'),
    path('toggleshop', toggle_shop, name='toggleshop'),
    path('additem', add_item, name='additem'),
    path('acceptorder', accept_order, name='acceptorder'),
    path('cancelorder', cancel_order, name='cancelorder'),
    path('getavailableorder', get_available_order, name='getavailableorder'),
    path('assignorder', assign_order, name='assignorder'),
    path('finishordertask', finish_order_task, name='finishordertask'),
    path('getorderstatus', get_order_status, name='getorderstatus'),
]