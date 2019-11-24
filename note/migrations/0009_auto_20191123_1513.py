# Generated by Django 2.2 on 2019-11-23 14:13

from django.db import migrations, models
import note.validators


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0008_auto_20191117_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='deadline',
            field=models.DateTimeField(validators=[note.validators.deadline_validator]),
        ),
    ]
