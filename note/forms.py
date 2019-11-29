from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms

from note.models import *


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


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageToNote
        fields = ['description', 'image']