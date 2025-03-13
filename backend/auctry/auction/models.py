from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User


class auctons(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, primary_key=True)
    amount = models.FloatField(default=0)


class Items(models.Model):
    name = models.CharField(
        max_length=250, null=False, blank=False, default="item_name"
    )
    initial_price = models.FloatField(null=False, blank=False)
    step_price = models.FloatField(
        default=1,
        null=False,
        blank=False,
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="item_seller",
    )
    description = models.TextField(null=False, blank=False, default=None)
    deadline = models.DateTimeField(null=True, blank=True, default=None)
    date_started = models.DateTimeField(auto_now_add=True)
    is_delivery_fees = models.BooleanField(null=False, blank=False, default=None)
    on_sale = models.BooleanField(null=False, blank=False, default=True)

class Bids(models.Model):
    item=models.ForeignKey(Items,on_delete=models.CASCADE,related_name="item")
    bidder = models.ForeignKey(User,on_delete=models.CASCADE,related_name="item")
    bid = models.FloatField()