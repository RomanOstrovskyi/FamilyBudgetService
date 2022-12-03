from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinLengthValidator


class Profile(models.Model):

    SpendingLimit = models.IntegerField(blank=False, default=0)
    RegisteredDay = models.DateTimeField(auto_now_add=True)
    Family = models.ForeignKey('Family', on_delete=models.CASCADE)
    FamilyRole = models.ForeignKey('FamilyRole', on_delete=models.CASCADE)

    def __str__(self):

        return f"Username : {User.username}, First name: {User.first_name}, Last name: {User.last_name}," \
               f" Email : {User.email}, Registered on : {self.RegisteredDay}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Family(models.Model):

    Family_id = models.AutoField(primary_key=True)
    FamilyName = models.CharField(max_length=24, blank=False, default='New_Family', validators=[MinLengthValidator(3)])
    FamilyMembers = models.IntegerField(blank=False)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"Family name : {self.FamilyName}, Creation date: {self.CreationDate}"


class FamilyRole(models.Model):

    ROLE = (
        ('Administrator', 'Administrator'),
        ('Member', 'Member'),
    )

    FamilyRole_id = models.AutoField(primary_key=True)
    Role = models.CharField(max_length=14, blank=False, choices=ROLE, default='Member',
                            validators=[MinLengthValidator(3)])

