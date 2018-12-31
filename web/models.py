from __future__ import  unicode_literals
from django.db import models
from django.contrib.auth.models import User


from django.db.models import BigIntegerField

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token= models.CharField(max_length=48)
    def __str__(self):
        return '{}-Token'.format(self.user)

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    def __str__(self):
        return "{}-{}".format(self.date , self.amount)

class Income(models.Model):
    text= models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete = models.DO_NOTHING)
    def __str__(self):
        return "{}-{}".format(self.date , self.amount)