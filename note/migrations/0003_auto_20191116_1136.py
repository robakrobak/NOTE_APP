# Generated by Django 2.2 on 2019-11-16 11:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0002_auto_20191116_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noteuser',
            name='id_user',
        ),
        migrations.AddField(
            model_name='noteuser',
            name='id_user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
