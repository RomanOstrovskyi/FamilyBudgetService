# Generated by Django 4.1.2 on 2022-12-05 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_profile_user'),
        ('Budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='Family',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Users.family'),
        ),
    ]
