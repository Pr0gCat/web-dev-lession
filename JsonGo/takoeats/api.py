from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def get_random_opened_shop(request):
    pass

"""
商店管理
"""
@login_required
def close_shop(request):
    pass

@login_required
def open_shop(request):
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

