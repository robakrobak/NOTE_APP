from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView

from note.filters import NoteFilter
from note.models import Note


class NotesListView(ListView):
    model = Note
    template_name = "home.html"
    done = False
    ordering = 'deadline'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            return queryset.filter(Q(id_users=self.request.user) | Q(created_by=self.request.user),
                                   is_done=self.done).distinct()
        else:
            return Note.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NoteFilter(self.request.GET, queryset=self.get_queryset())
        return context


def logout_view(request):
    logout(request)
    return redirect('/')


class NotesListArchiveView(NotesListView):
    model = Note
    template_name = "archive.html"
    done = True
    ordering = '-deadline'
