from django import forms


class SingninForm(forms.Form):
    username = forms.CharField(
        label='Nome de usuario',
        max_length=128,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuario'
            }),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
            }),
        max_length=32,
    )
