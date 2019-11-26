from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from django.forms.widgets import Textarea


from note.models import Note, Comment


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note', 'deadline', 'id_users']
        labels = {'id_users': 'Users added to note'}

        widgets = {
            'deadline': DateTimePickerInput(),  # default date-format %m/%d/%Y will be used
            'note': forms.Textarea(),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': '' }
        # widgets = {
        #     'text': forms.Textarea(),
        # }
