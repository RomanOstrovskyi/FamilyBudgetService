# Generated by Django 4.1.2 on 2022-12-03 13:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('Credit_card_id', models.AutoField(primary_key=True, serialize=False)),
                ('Bank_name', models.CharField(max_length=99, validators=[django.core.validators.MinLengthValidator(2)])),
                ('Card_number', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(16), django.core.validators.MinLengthValidator(16)])),
                ('CVV', models.IntegerField(validators=[django.core.validators.MinLengthValidator(3)])),
                ('Balance_UAH', models.IntegerField(default=0)),
                ('Balance_USD', models.IntegerField(default=0)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]