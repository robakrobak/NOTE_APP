from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout




def home(request):
    return render(request, 'home.html', {})


def logout_view(request):
    logout(request)
    return redirect('/')
