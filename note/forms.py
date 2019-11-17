from django import forms
from note.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = {'title': "Title", 'note': "Note", 'deadline': "Deadline", 'id_users': "Coworkers"}
