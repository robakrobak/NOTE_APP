# django
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
# python
from note.models import Note
from note.forms import NoteForm


def note(request):
    return render(request, "note.html", {'notes': Note.objects.all()})


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    success_url = "/note"
    template_name = "add_note.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)