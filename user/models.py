from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    awatar = models.FileField(upload_to='awatar')
    about_me = models.CharField(max_length=512)

    def __str__(self):
        return self.user.username


