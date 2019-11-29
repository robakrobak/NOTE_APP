# Generated by Django 2.2 on 2019-11-24 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0010_auto_20191124_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='priority',
            field=models.CharField(choices=[('L', 'LOW'), ('M', 'MEDIUM'), ('H', 'HIGH'), ('', 'NO_PRIORITY')], default='', max_length=1),
        ),
    ]
