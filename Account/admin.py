from django.contrib import admin
from Account.models import User_create, User_Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'email', 'is_active', 'is_superuser', 'is_staff']

    class Meta:
        models = User_create


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['author', 'firstname', 'lastname', 'address']

    class Meta:
        models = User_Profile

# Register your models here.
admin.site.register(User_create, UserAdmin)
admin.site.register(User_Profile, UserProfileAdmin)

