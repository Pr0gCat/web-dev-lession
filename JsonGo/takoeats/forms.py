from django import forms
from django.contrib.auth.models import User

from .models import Item

class LoginForm(forms.Form):
    username = forms.CharField(label='用戶名稱', max_length=64, required=True)
    password = forms.CharField(label='密碼', max_length=64, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(forms.Form):
    display_name = forms.CharField(label='顯示名稱', max_length=16, required=True)
    contact = forms.CharField(label='電話號碼', max_length=10, required=True)
    username = forms.CharField(label='用戶名稱', max_length=16, required=True)
    password = forms.CharField(label='密碼', max_length=64, widget=forms.PasswordInput(), required=True)
    password_confirm = forms.CharField(label='確認密碼', max_length=64, widget=forms.PasswordInput(), required=True)
    class Meta:
        model = User
        fields = ('display_name', 'contact', 'username', 'password', 'password_confirm')

class InfoUpdateForm(forms.Form):
    display_name = forms.CharField(label='顯示名稱', max_length=16, required=False)
    contact = forms.CharField(label='電話號碼', max_length=10, required=False)
    address = forms.CharField(label='地址', max_length=64, required=False)
    class Meta:
        model = User
        fields = ('display_name', 'contact', 'address')

class AddItemForm(forms.Form):
    name = forms.CharField(label='名稱', max_length=16, required=True)
    price = forms.DecimalField(label='價格', max_digits=6, decimal_places=2, required=True)
    status = forms.IntegerField(label='上架', required=True)
    category = forms.CharField(label='類別', max_length=16, required=True)
    desc = forms.CharField(label='描述', max_length=100, required=False)
    image = forms.ImageField(label='圖片', required=False)
    class Meta:
        model = Item
        fields = "__all__"