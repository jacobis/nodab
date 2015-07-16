from django.contrib import admin

from .models import User, Boss, UserBoss

admin.site.register(User)
admin.site.register(Boss)
admin.site.register(UserBoss)