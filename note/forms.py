from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms

from note.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note', 'deadline', 'id_users']
        labels = {'id_users': 'Users added to note'}
        priority_choices = {'priority': 'Notes priority'}

        widgets = {
            'deadline': DateTimePickerInput(),  # default date-format %m/%d/%Y will be used
            'note': forms.Textarea(),
            'priority': forms.CheckboxSelectMultiple,
        }
 # status = forms.ChoiceField(choices = STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)