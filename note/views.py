from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
# python
from note.forms import NoteForm, CommentForm
from note.models import Note
from core.email_service import note_assign_mail


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
            note_assign_mail(form.cleaned_data.get('id_users'), form.cleaned_data.get('title'))
        return variable


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = 'home'
    model = Note
    form_class = NoteForm
    success_url = "/"
    template_name = "edit_note.html"
    mail_list = []
    for user in self.object.id_users.all():
        mail_list.append(user)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            return queryset.filter(created_by=self.request.user, pk=self.kwargs['pk'])
        else:
            return Note.objects.none()

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        variable = super().form_valid(form)
        if variable:
            for user in self.object.id_users.all():
                if user not in self.mail_list:
                    note_assign_mail([user], form.cleaned_data.get('title'))
        return variable


def change_status(request, pk, done):
    note = Note.objects.get(pk=pk)
    if note.created_by == request.user:
        note.change_status(bool(done))
        if done == 0:
            return redirect('/archive')
        else:
            return redirect('/')
    else:
        return redirect('notes/add/')


class NoteDetailView(DetailView, FormMixin):
    model = Note
    template_name = "note_detail.html"
    context_object_name = "note"
    form_class = CommentForm

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            return queryset.filter(Q(id_users=self.request.user) | Q(created_by=self.request.user),
                                   pk=self.kwargs['pk']).distinct()
        else:
            return Note.objects.none()

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid() and len(form.instance.text) > 0:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.note = self.get_object()
        form.save()
        return HttpResponseRedirect(self.request.path_info)
