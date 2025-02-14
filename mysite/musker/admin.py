from django.contrib import admin

from django.contrib.auth.models import Group, User
from .models import Profile, Meep

# Unregister the Group model from admin. Remove it from the admin panel.
admin.site.unregister(Group)

# Extend User Nodel


# Mix Profile info User info in the admin panel
class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User

    # Display username fields in the admin panel
    fields = ["username"]

    # Display Profile info in the admin panel
    inlines = [ProfileInline]


# Unregister initial Users.
admin.site.unregister(User)

# Register USer and Profile models
admin.site.register(User, UserAdmin)

# admin.site.register(Profile)

# Register Meep and Profile models
admin.site.register(Meep)
