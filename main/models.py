from django.db import models


class Zombie(models.Model):
    name = models.CharField(max_length=50)
    cementery = models.CharField(max_length=100)


class Tweet(models.Model):
    status = models.CharField(max_length=150)
    zombie = models.ForeignKey('Zombie', related_name='tweets')
    created_at = models.DateTimeField(auto_now_add=True)
