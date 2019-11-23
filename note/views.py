# django
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        variable = super().form_valid(form)
        # import ipdb;
        # ipdb.set_trace()
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
        return redirect('note/add/')

