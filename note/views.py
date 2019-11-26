from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
# python
from note.forms import NoteForm, CommentForm
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
                message=f"You have been assigned to note '{form.cleaned_data.get('title')}'."
                        f"Check your current status at NOTE_APP application",
                from_email="noteapp12345@gmail.com",
                recipient_list=[user.email for user in form.cleaned_data.get('id_users')])
        return variable


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = 'home'
    model = Note
    form_class = NoteForm
    success_url = "/"
    template_name = "edit_note.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            return queryset.filter(created_by=self.request.user, pk=self.kwargs['pk'])
        else:
            return Note.objects.none()


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


class NoteDetailView(DetailView):
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

    # def get_context_data(self, **kwargs):
    #     context = super(NoteDetailView, self).get_context_data(**kwargs)
    #     context['form'] = CommentForm(initial={
    #         'note': self.object, 'author': self.request.user
    #     })
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.get_form()
    #
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    #
    # def form_valid(self, form):
    #     form.save()
    #     return super(NoteDetailView, self).form_valid(form)


def add_comment_to_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.note = note
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()
    return render(request, 'note_detail.html', {'form': form})
