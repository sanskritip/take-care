# Generated by Django 3.0.4 on 2020-04-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='fullname',
            field=models.CharField(default='fullname unupdated', max_length=200),
        ),
    ]
