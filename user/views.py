# python
from user.forms import SignUpForm
from core.email_service import confirms_registration
# django
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.core.mail import send_mail


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'index.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


#
# def logout_view(request):
#     logout(request)
#     pass


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            email = form.cleaned_data.get('email')
            login(request, user)
            confirms_registration(email, username, raw_password)
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
