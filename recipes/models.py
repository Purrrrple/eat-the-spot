from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Ingredient(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# A Recipe is a post including a list of editable ingredients
class Recipe(models.Model):
    #Generic post fields
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #Recipe fields
    ingredients = models.ManyToManyField(Ingredient, through='Amount')

    def __str__(self):
        return self.title


class Amount(models.Model):
    recipe = models.ForeignKey (Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey (Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5,decimal_places=2)
    calories = models.PositiveSmallIntegerField()
    brand = models.CharField(max_length=128)
