from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from allauth.socialaccount.models import SocialAccount


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'username', 'email', 'role',
                    'is_verified', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
         'fields': ('role', 'phone_number', 'profile_picture', 'is_verified')}),
    )


# try:
#     admin.site.register(SocialAccount)
# except AlreadyRegistered:
#     pass

if not admin.site.is_registered(SocialAccount):
    admin.site.register(SocialAccount)

admin.site.register(CustomUser, CustomUserAdmin)
