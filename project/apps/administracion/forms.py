from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }
        help_texts = {k: "" for k in fields}

class UserUpdateForm(forms.ModelForm):
    usuario = forms.CharField(label='Nombre de usuario', max_length=150)
    contraseña_anterior = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput)
    contraseña_nueva = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    confirmacion_contraseña_nueva = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['usuario', 'contraseña_anterior', 'contraseña_nueva', 'confirmacion_contraseña_nueva']