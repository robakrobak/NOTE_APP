from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormMixin, DeleteView
from django.db.models import Q
from django.http import HttpResponseRedirect
# python
from note.forms import NoteForm, CommentForm, ImageForm
from note.models import Note, ImageToNote
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mail_list = []

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            return queryset.filter(created_by=self.request.user, pk=self.kwargs['pk'])
        else:
            return Note.objects.none()

    def form_valid(self, form):
        for user in self.object.id_users.all():
            self.mail_list.append(user)
        variable = super().form_valid(form)
        if variable:
            for user in form.cleaned_data.get('id_users'):
                if user not in self.mail_list:
                    note_assign_mail([user], form.cleaned_data.get('title'))
            self.mail_list = []
            return redirect('note_detail', pk=self.kwargs['pk'])


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


class ImageCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = 'home'
    model = ImageToNote
    form_class = ImageForm
    template_name = "add_image.html"

    def form_valid(self, form):
        try:
            form.instance.note = Note.objects.get(pk=self.kwargs['pk'], created_by=self.request.user)
            form.instance.created_by = self.request.user
            form.save()
        finally:
            return redirect('note_detail', pk=self.kwargs['pk'])


def delete_image(request, imgpk, pk):
    try:
        query = ImageToNote.objects.get(pk=imgpk, created_by=request.user)
        print(query)
        query.delete()
    finally:
        return redirect('note_detail', pk=pk)
