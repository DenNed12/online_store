from django.db import models
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length= 64,
        unique = True
    )
    description = models.TextField()
    quantity = models.IntegerField(validators = [MinValueValidator(0)])
    category = models.ForeignKey(
        to ='Category',
        on_delete=models.CASCADE,
        related_name = 'products'
    )
    price = models.FloatField(
        validators = [MinValueValidator(0.0)])


    def __str__(self):
        return f'{self.name.title()} : {self.description[20:]} '

    added_at = models.DateTimeField(
        auto_now=True,
    )

class Category(models.Model):
    name = models.CharField(max_length=200, unique =True)

    def __str__(self):
        return self.name.title()



class Subscription(models.Model):
    user = models.ForeignKey(
        to= User,
        on_delete= models.CASCADE,
        related_name='subscriptions')
    category  = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name ='subscriptions'
    )