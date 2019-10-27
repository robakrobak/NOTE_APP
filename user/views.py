from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return print("zalogowany")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#
# def logout_view(request):
#     logout(request)
#     pass
