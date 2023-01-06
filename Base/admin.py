from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserManager
from Base.models import User, Verification, Post

admin.site.register(User)
admin.site.register(Verification)
admin.site.register(Post)
admin.site.unregister(Group)