from django.db import models

from note.validators import deadline_validator
from user.models import User

from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=128, null=False)
    note = models.CharField(max_length=4096)
    add_date = models.DateTimeField(auto_now_add=True, null=False)
    created_by = models.ForeignKey(User, default=None, blank=False, on_delete=models.CASCADE, null=True,
                                   related_name='note_creator')
    deadline = models.DateTimeField(null=False, blank=False, validators=[deadline_validator])
    is_done = models.BooleanField(default=False, blank=False)
    id_users = models.ManyToManyField(User, blank=True, related_name='users_pinned_to_note')

    def __str__(self):
        return self.title

    def change_status(self, done):
        self.is_done = done
        self.save()


class Comment(models.Model):
    note = models.ForeignKey('note.Note', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, default=None, blank=False, on_delete=models.CASCADE, null=True,
                               related_name='comment_creator')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
