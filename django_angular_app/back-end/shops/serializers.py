from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Item ,Cart


class CartSerializer(serializers.ModelSerializer):
    #items = serializers.StringRelatedField(read_only=True,many=True)
    class Meta:
        model = Cart
        fields = ('id','userId', 'item_id','date_creation')

class ItemSerializer(serializers.ModelSerializer):
    carts = CartSerializer(read_only=True,many=True)
    class Meta:
        model = Item
        fields = ('id','titre', 'description', 'img_url', 'pub_date','carts')


# this two class for default auth in django (models User, Goup)
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')