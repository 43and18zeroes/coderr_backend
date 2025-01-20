# Generated by Django 5.1.5 on 2025-01-20 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0005_alter_userprofile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='file',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tel',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='working_hours',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]