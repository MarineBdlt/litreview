# Generated by Django 4.0.1 on 2022-03-10 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_userfollows_userfollow_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]