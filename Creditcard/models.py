from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models import Model


class CreditCard(models.Model):

    Credit_card_id = models.AutoField(primary_key=True)
    Bank_name = models.CharField(max_length=99, validators=[MinLengthValidator(2)],
                                 blank=False)
    Card_number = models.IntegerField(validators=[MaxLengthValidator(16), MinLengthValidator(16)])
    CVV = models.IntegerField(validators=[MinLengthValidator(3)], blank=False)
    Balance_UAH = models.IntegerField(blank=False, default=0)
    Balance_USD = models.IntegerField(blank=False, default=0)
    User = models.ForeignKey(User, blank=False, on_delete=models.PROTECT)

    def __str__(self):

        return f"Owner : {self.User}, UAH left: {self.Balance_UAH}, USD left: {self.Balance_USD}, Bank name : {self.Bank_name},"


#
