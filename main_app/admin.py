from main_app.models import Subscription
from django.contrib import admin
from .models import Photo, Purchase, Subscription

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Purchase)
admin.site.register(Photo)