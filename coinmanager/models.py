from django.db import models
from django.utils import timezone

# Create your models here.
class Coin(models.Model):
    author = models.ForeignKey('auth.User')
    value = models.IntegerField()
    country = models.CharField(max_length=20)
    released_year = models.IntegerField()
    link2pic = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.country