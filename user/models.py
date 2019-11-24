from django.contrib.auth.models import User
from django.db import models


User._meta.get_field('email')._unique = True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    awatar = models.FileField(upload_to='awatar', blank=True, default='awatar/default-100.png')
    about_me = models.CharField(max_length=512, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
