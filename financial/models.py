from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Shares(models.Model):
    code = models.CharField(max_length=6)
    company = models.CharField(max_length=128, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    def __str__(self):
        return self.code


class UserShares(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='my_shares')
    share = models.ForeignKey(Shares, on_delete=models.PROTECT, related_name='users')
