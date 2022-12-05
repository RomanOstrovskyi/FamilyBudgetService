# Generated by Django 4.1.2 on 2022-12-05 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='User',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]