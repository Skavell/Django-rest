from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
# from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .models import BoardGame, Category, Order, OrderItem, Review

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer, BoardGameSerializer, OrderSerializer, \
    CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class BoardGameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows boardgames to be viewed or edited.
    """
    queryset = BoardGame.objects.all().order_by('id')
    serializer_class = BoardGameSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category__name']
    ordering_fields = ['title', 'price', 'category']
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def price_avg(self, request):
        summ = 0
        boardgames = BoardGame.objects.all()
        for boardgame in boardgames:
            summ += boardgame.price
        avg = summ / len(boardgames)
        return Response(avg)


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all().order_by('date_ordered')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all().order_by('date_ordered')
        return Order.objects.filter(
            Q(user=user.id) & Q(complete=False)
        ).order_by('date_ordered')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
