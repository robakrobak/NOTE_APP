from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from note.forms import NoteForm
from note.models import Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = 'home'
    model = Note
    form_class = NoteForm
    success_url = "/"
    template_name = "add_note.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        variable = super().form_valid(form)
        if variable:
            send_mail(
                subject="You have been assigned(...)",
                message="You have beed assigned to note. Check your current status at NOTE_APP application",
                from_email="noteapp12345@gmail.com",
                recipient_list=[user.email for user in form.cleaned_data.get('id_users')])
        return variable


def mark_as_done(request, pk):
    note = Note.objects.get(pk=pk)
    if note.created_by == request.user:
        note.mark_as_done()
        return redirect('/')
    else:
        return redirect('notes/add/')


class NoteDetailView(DetailView):
    model = Note
    template_name = "note_detail.html"
    context_object_name = "note"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if Note.objects.filter(created_by=self.request.user):
                return Note.objects.filter(created_by=self.request.user)
            else:
                return Note.objects.filter(id_users=self.request.user)
        else:
            return Note.objects.none()
