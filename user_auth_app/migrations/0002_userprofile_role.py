# Generated by Django 5.1.5 on 2025-01-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('provider', 'Provider')], default='customer', max_length=10),
        ),
    ]
