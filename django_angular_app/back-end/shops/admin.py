from django.contrib import admin

# Register your models here.
from .models import Item
from .models import Cart

admin.site.register(Item)
admin.site.register(Cart)