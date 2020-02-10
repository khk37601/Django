from django import forms
from django.contrib.auth.models import User
from django.db import models


class Rank(models.Model):

    index = models.BigIntegerField(primary_key=True)
    word = models.CharField(max_length=20)
    update_date = models.DateField()



