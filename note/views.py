# django
from django.shortcuts import redirect, render
from note.models import Note


def note(request):
    return render(request, "note.html", {'notes': Note.objects.all()})
