# django
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from note.forms import NoteForm
from django.shortcuts import redirect

# python
from note.models import Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = 'home'
    model = Note
    form_class = NoteForm
    success_url = "/"
    template_name = "add_note.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def mark_as_done(request, pk):
    note = Note.objects.get(pk=pk)
    if note.created_by == request.user:
        note.mark_as_done()
        return redirect('/')
    else:
        return redirect('note/add/')
