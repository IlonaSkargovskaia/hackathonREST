from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    # favorited_by = models.ManyToManyField(User, related_name='favorite_recipes')
    favorite = models.BooleanField(default=False)
    img = models.URLField()
    ingredients = models.ManyToManyField('Ingredient', related_name='recipes')
    video = models.URLField()

    def __str__(self):
        return self.title


