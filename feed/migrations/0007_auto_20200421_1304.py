# Generated by Django 3.0.4 on 2020-04-21 07:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('feed', '0006_merge_20200421_0235'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Save',
            new_name='Saves',
        ),
    ]
