from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3,unique=True)
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.code

class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='categories')
    name = models.CharField(max_length=32,blank=True)

    def __str__(self) -> str:
        return self.name

class Transactions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='transactions')
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,related_name='transactions')
    date = models.DateTimeField()
    desc = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='trasanctions')

    def __str__(self) -> str:
        return f"{self.amount} {self.currency.code} {self.date}"


