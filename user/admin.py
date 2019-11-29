from django.contrib import admin
from user.models import UserProfile
from note.models import Note, Comment, ImageToNote


admin.site.register(UserProfile)
admin.site.register(Note)
admin.site.register(Comment)
admin.site.register(ImageToNote)