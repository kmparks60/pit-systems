from django.contrib import admin
from .models import Business, CustomUser

admin.site.register(Business)
admin.site.register(CustomUser)