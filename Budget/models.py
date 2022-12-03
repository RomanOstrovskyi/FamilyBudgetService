from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
from Users.models import Family


class Budget(models.Model):

    Budget_id = models.AutoField(primary_key=True)
    UAH_amount = models.IntegerField(blank=False, default=0)
    USD_amount = models.IntegerField(blank=False, default=0)
    Date_created = models.DateTimeField(auto_now_add=True)
    Creator = models.ForeignKey(User, on_delete=models.CASCADE)
    Family = models.ForeignKey(Family, default=1, on_delete=models.CASCADE)

    def __str__(self):

        return f"Creator : {self.Creator}, UAH: {self.UAH_amount}, USD: {self.USD_amount}," \
               f" Created date : {self.Date_created},"


class TransactionHistory(models.Model):

    TH_id = models.AutoField(primary_key=True)
    Currency = models.CharField(max_length=30, blank=False, validators=[MinLengthValidator(3)])
    TransactionTime = models.DateTimeField(auto_now_add=True, blank=False)
    Sender_id = models.CharField(max_length=1638, validators=[MinLengthValidator(1)], blank=False)
    Receiver_id = models.CharField(max_length=1638, validators=[MinLengthValidator(1)], blank=False)
    User = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    Budget = models.ForeignKey(Budget, blank=False, on_delete=models.CASCADE)

    def __str__(self):

        return f"Sender : {self.Sender_id}, Receiver: {self.Receiver_id}, Currency: {self.Currency}," \
               f" Transaction number : {self.TH_id},"

