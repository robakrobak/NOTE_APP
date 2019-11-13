from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout


# def background_test(request):
#     return HttpResponse("Hello, world. Checkout background.")

def home(request):
    return render(request, 'home.html', {})


def logout_view(request):
    return logout(request, 'home.html', {})
