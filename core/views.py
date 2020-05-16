from django.shortcuts import render, redirect
from core.forms import SingninForm
from django.contrib.auth import authenticate, login


# Create your views here.
def homepage(request):
    return redirect('dashboard_index')


def login_view(request):
    if request.method != 'POST':
        return render(request, 'login.html', {'form': SingninForm(), 'login_page': True})

    form = SingninForm(request.POST)
    if not form.is_valid():
        return render(request, 'login.html', {'form': form})

    username = form.cleaned_data.get('username').lower()
    password = form.cleaned_data.get('password')

    user = authenticate(username=username, password=password)
    if not user or not user.is_active:
        return render(request, 'login.html', {'form': form, 'login_page': True, 'login_error': True})

    login(request, user)
    return redirect('dashboard_index')
