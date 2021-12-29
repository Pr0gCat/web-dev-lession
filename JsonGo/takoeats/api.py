from django.urls import path
from django.contrib.auth.decorators import login_required

def get_random_opened_shop(request):
    pass

"""
商店管理
"""
@login_required
def open_shop(request):
    """
        post:
            商店開店
            params: 's' - 1: 開店, 0: 關店
        get:
            得取狀態
    """
    pass

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
    path('openshop', open_shop, name='openshop'),
    path('acceptorder', accept_order, name='acceptorder'),
    path('cancelorder', cancel_order, name='cancelorder'),
    path('getavailableorder', get_available_order, name='getavailableorder'),
    path('assignorder', assign_order, name='assignorder'),
    path('finishordertask', finish_order_task, name='finishordertask'),
    path('getorderstatus', get_order_status, name='getorderstatus'),
]