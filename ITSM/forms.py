from django.contrib.auth.models import User
from django import forms
from .models import ITSM_User_Model

class PasswordResetForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário', max_length=150)
    new_password = forms.CharField(label='Nova Senha', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data
    
    def save(self):
        username = self.cleaned_data['username']
        new_password = self.cleaned_data['new_password']

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
        except User.DoesNotExist:
            raise forms.ValidationError("Usuário não encontrado.")

class UserForm(forms.Form):
    username = forms.CharField(label='Login', max_length=150)
    first_name = forms.CharField(label='Nome', max_length=30, required=False)
    last_name = forms.CharField(label='Sobrenome', max_length=30, required=False)
    email = forms.EmailField(label='Email', required=False)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput, required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password or confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data
    
    def save(self, user_instance=None):
        if user_instance:
            user = user_instance
        else:
            user = ITSM_User_Model()

        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        user.email = self.cleaned_data.get('email', '')

        password = self.cleaned_data.get('password', '')
        if password:
            user.senha = password

        user.save()
        return user