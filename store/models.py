from django.db import models
from uuid import uuid5
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name='category', max_length=255)

    def __str__(self) -> str:
        return self.title


class menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    orderdate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title} {self.id}'


class cart(models.Model):
    cartid = models.URLField(primary_key=True, default=uuid5, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cartid


class booking(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    modifed = models.DateField(auto_now=True)

    def __str__(self):
        return self.id


class delivery(models.Model):
    price = models.ForeignKey(menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(booking, on_delete=models.CASCADE)

def __str__(self):
        return f'{self.price} {self.order.cart.cart_id} {self.order.cart.user}'

