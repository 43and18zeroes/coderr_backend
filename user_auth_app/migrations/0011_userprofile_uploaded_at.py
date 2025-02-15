# Generated by Django 5.1.5 on 2025-02-15 15:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0010_remove_userprofile_uploaded_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
