from django.contrib.auth.models import Group, User
from rest_framework import serializers

from tutorial.quickstart.models import BoardGame, Order, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name']


class BoardGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardGame
        fields = ['url', 'id', 'title', 'price', 'category', 'image']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'id', 'user', 'date_ordered', 'complete']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name']
