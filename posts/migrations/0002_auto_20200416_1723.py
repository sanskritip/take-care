# Generated by Django 3.0.4 on 2020-04-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name=''),
        ),
    ]
