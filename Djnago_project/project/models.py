from django.db import models


# Create your models here.
class Rank(models.Model):
    index = models.BigIntegerField(primary_key=True)
    word = models.CharField(max_length=20)
    update_date = models.DateTimeField(auto_now_add=True)


class Email(models.Model):
    email = models.CharField(max_length=100, blank=True, primary_key=True)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

class PremierLeague2(models.Model):

    rank = models.IntegerField()
    team_name = models.CharField(max_length=35, primary_key=True)
    winning = models.IntegerField()

    class Meta:
        ordering = ['rank',]

    def __str__(self):
        return self.team_name



