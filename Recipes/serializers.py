from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ingredients, Comment, Recipes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'rating']

class RecipesSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    ingredients = IngredientsSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Recipes
        fields = ['id', 'author', 'ingredients', 'comments']
