# Generated by Django 3.1.3 on 2021-01-03 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20201231_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place_permission',
            name='delete_time',
        ),
        migrations.RemoveField(
            model_name='place_permission',
            name='is_delete',
        ),
    ]
