# Generated by Django 5.1.2 on 2024-11-28 19:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_options_remove_post_attached_files_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='postfiles',
            old_name='id_post',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id_user',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]