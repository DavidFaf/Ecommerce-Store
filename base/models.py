from email.policy import default
from enum import auto
from django.db import models

from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from taggit.managers import TaggableManager

class UserModel(AbstractUser):
    username = None
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Item(models.Model):
    item_name = models.CharField(max_length = 200)
    serial_number = models.CharField(max_length = 15)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    description = models.TextField()
    tags = TaggableManager()
    # owner = "Who owns an item"

    def __repr__(self):
        return f'Item {self.item_name}'

class Order(models.Model):
    customer = models.ForeignKey(UserModel, on_delete=models.SET_NULL, blank=True, null=True)
    reference_no =  models.CharField(max_length = 200, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    def __repr__(self):
        return f'Order {self.reference_no}'

    @property
    def get_cart_total(self):
        orderItems = self.orderitems_set.all()
        total = sum([item.get_total for item in orderItems])
        return total

    @property
    def get_cart_items(self):
        orderItems = self.orderitems_set.all()
        total = sum([item.item_quantity for item in orderItems])
        return total


class OrderItems(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    item_quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add= True)

    @property
    def get_total(self):
        total = self.item_quantity * self.item.price
        return total 

