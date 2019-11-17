from django.contrib import admin
from user.models import UserProfile
from note.models import Note

admin.site.register(UserProfile)
admin.site.register(Note)
