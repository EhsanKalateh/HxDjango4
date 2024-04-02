from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
    "username",
    "first_name",
    "last_name",
    "field",
    "degree",
    "university",
    "is_article_author",
    "is_article_editor",
    "is_case_editor",
    "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("university","degree")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("university","degree")}),)
    list_display_links = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
