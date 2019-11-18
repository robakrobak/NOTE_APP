from django.contrib.auth.models import User
from django.db import models

# from django.dispatch import receiver
# from django.db import models
# from django.db.models.signals import post_save

User._meta.get_field('email')._unique = True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    awatar = models.FileField(upload_to='awatar', blank=True)
    about_me = models.CharField(max_length=512, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
