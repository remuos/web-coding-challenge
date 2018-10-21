from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from .models import Item ,Cart
from shops.serializers import ItemSerializer, CartSerializer, UserSerializer, GroupSerializer


def index(request):
    return render(request, 'index.html')

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows can filter the data
    if the param userId exist return the preferred shop by the user(pk=userId)
    if the param not_userId exist exclude the preferred shop by the user(pk=not_userId)
    """
    queryset = Item.objects.all().order_by('-pub_date')
    serializer_class = ItemSerializer

    def list(self, request):
        if request.GET.get('userId') :
            queryset = Item.objects.filter(carts__userId =request.GET.get('userId'))
        elif request.GET.get('not_userId') :
            queryset = Item.objects.exclude(carts__userId =request.GET.get('not_userId'))
        else:
            queryset = Item.objects.all()
        
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows carts to be viewed or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



# default auth 

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer