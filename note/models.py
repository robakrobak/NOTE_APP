from django.db import models
from user.models import User


class Note(models.Model):
    title = models.CharField(max_length=32, null=False)
    note = models.CharField(max_length=4096)
    add_date = models.DateTimeField(auto_now_add=True, null=False)
    deadline = models.DateField(null=False, blank=False)
    is_done = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.title


class NoteUser(models.Model):
    id_note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True)
    id_user = models.ManyToManyField(User, blank=True)


