# python
from note.models import Note
from note.filters import NoteFilter
# django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.views.generic import ListView
from django.db.models import Q


class NotesListView(ListView):
    model = Note
    template_name = "home.html"
    ordering = ['deadline']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            return queryset.filter(Q(id_users=self.request.user) | Q(created_by=self.request.user), is_done=False).distinct()
        else:
            return Note.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NoteFilter(self.request.GET, queryset=self.get_queryset())
        return context


def logout_view(request):
    logout(request)
    return redirect('/')

  
class NotesListArchiveView(ListView):
    model = Note
    template_name = "archive.html"
    context_object_name = "notes"

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['notes'] = Note.objects.filter(Q(id_users=self.request.user) | Q(created_by=self.request.user),
                                                   is_done=True, ).order_by("deadline").distinct
        except:
            context = super().get_context_data(**kwargs)
            context['notes'] = None
        return context


