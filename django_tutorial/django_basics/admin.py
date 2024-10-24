from django.contrib import admin
# Register your models here.
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _text

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_text("Personal info"), {"fields": ("first_name", "last_name", "photo")}),
        (
            _text("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_text("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("usable_password", "password1", "password2"),
            },
        ),
    )

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User, MyUserAdmin)