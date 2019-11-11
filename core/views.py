from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Registration complete. You have been bamboozled.\nLet get to the real stuff.")
