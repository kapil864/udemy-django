# Generated by Django 5.0.3 on 2024-03-24 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_image',
            new_name='image',
        ),
    ]
