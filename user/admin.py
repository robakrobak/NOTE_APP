from django.contrib import admin
from user.models import UserProfile
from note.models import Note, Comment


admin.site.register(UserProfile)
admin.site.register(Note)
admin.site.register(Comment)
