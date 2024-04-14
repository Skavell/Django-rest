from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()


class BoardGame(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='boardgames/')
    history = HistoricalRecords()
    objects = models.Manager()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    objects = models.Manager()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    objects = models.Manager()


class Review(models.Model):
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
