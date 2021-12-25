from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='用戶名稱', max_length=64, required=True)
    password = forms.CharField(label='密碼', max_length=64, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(forms.Form):
    display_name = forms.CharField(label='顯示名稱', max_length=16, required=True)
    contact_number = forms.CharField(label='聯絡電話', max_length=10, required=True)
    username = forms.CharField(label='用戶名稱', max_length=16, required=True)
    password = forms.CharField(label='密碼', max_length=64, widget=forms.PasswordInput())
    password_confirm = forms.CharField(label='確認密碼', max_length=64, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('display_name', 'contact_no', 'username', 'password', 'password_confirm')