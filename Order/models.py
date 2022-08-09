from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.EmailField(null=False)
    password = models.CharField(max_length=100)
    address = models.TextField()


class Order(models.Model):
    class OrderStatus(models.IntegerChoices):
        placed = 1
        packed = 2
        dispatched =3
        delivered =4

    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered_on = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    status = models.IntegerField(choices=OrderStatus.choices)