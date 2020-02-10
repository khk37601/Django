from django.db import models


# Create your models here.
class PremierLeague(models.Model):

    rank = models.IntegerField()
    team_name = models.CharField(max_length=35, primary_key=True)
    winning = models.IntegerField()

    class Meta:
        ordering = ['rank']

    def __str__(self):
        return self.team_name
