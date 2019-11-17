from django.db import models
from django.contrib.auth.models import User

# from django.dispatch import receiver
# from django.db import models
# from django.db.models.signals import post_save

User._meta.get_field('email')._unique = True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    awatar = models.FileField(upload_to='awatar')
    about_me = models.CharField(max_length=512)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
