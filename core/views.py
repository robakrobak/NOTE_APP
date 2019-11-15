from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout




def home(request):
    return render(request, 'home.html', {})


def logout_view(request):
    return logout(request, 'home.html', {})
