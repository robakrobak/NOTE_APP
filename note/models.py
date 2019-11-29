import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import utc

from note.validators import deadline_validator
from user.models import User


class Note(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    NO_PRIORITY = 'no priority'
    priority_choices = [
        (NO_PRIORITY, 'no priority'),
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high'),

    ]
    title = models.CharField(max_length=128, null=False)
    note = models.CharField(max_length=4096)
    add_date = models.DateTimeField(auto_now_add=True, null=False)
    created_by = models.ForeignKey(User, default=None, blank=False, on_delete=models.CASCADE, null=True,
                                   related_name='note_creator')
    deadline = models.DateTimeField(null=False, blank=False, validators=[deadline_validator])
    is_done = models.BooleanField(default=False, blank=False)
    id_users = models.ManyToManyField(User, blank=True, related_name='users_pinned_to_note')
    priority = models.CharField(max_length=11, choices=priority_choices, default=NO_PRIORITY)

    def __str__(self):
        return self.title

    def change_status(self, done):
        self.is_done = done
        self.save()

    def get_time_diff(self):
        if self.deadline:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = self.deadline - now
            return timediff.total_seconds() / 3600


class Comment(models.Model):
    note = models.ForeignKey('note.Note', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, default=None, blank=False, on_delete=models.CASCADE, null=True,
                               related_name='comment_creator')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class ImageToNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='images')
    description = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media', blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.note.__str__() + 'image' + self.description