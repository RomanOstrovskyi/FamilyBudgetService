from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Budget(models.Model):

    Budget_id = models.IntegerField(primary_key=True)
    UAH_amount = models.IntegerField(blank=False, default=0)
    USD_amount = models.IntegerField(blank=False, default=0)
    Date_created = models.DateField(default=timezone.now())
    Creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):

        return f"Creator : {self.Creator}, UAH: {self.UAH_amount}, USD: {self.USD_amount}," \
               f" Created date : {self.Date_created},"
