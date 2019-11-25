import django_filters
from django.forms.widgets import TextInput

from note.models import Note


class NoteFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label="", lookup_expr='icontains',
                                      widget=TextInput(attrs={'placeholder': ' search'}))

    class Meta:
        model = Note
        fields = ['title']
