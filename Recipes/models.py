from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Ingredients(models.Model):
    name = models.CharField(max_length=20)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Recipes(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredients)
    comments = models.ManyToManyField(Comment)
