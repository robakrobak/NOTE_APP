# django
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from note.forms import NoteForm
from django.db.models import Q
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


class NoteDetailView(DetailView):
    model = Note
    template_name = "note_detail.html"
    context_object_name = "note"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(Q(id_users=self.request.user) | Q(created_by=self.request.user))
        else:
            return Note.objects.none()
