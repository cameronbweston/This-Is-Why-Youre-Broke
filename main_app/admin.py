from main_app.models import Subscription
from django.contrib import admin
from .models import Purchase, Subscription

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Purchase)