# Generated by Django 5.1.5 on 2025-02-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0007_alter_userprofile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_pics/'),
        ),
    ]
