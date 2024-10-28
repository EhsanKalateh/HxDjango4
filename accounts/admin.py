from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "first_name",
        "last_name",
        "degree",
        "university",
        "hx_cc_ai_permission",
        "is_staff",
        
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "field",
                    "university",
                    "degree",
                    "fn_fa",
                    "ln_fa",
                    "is_article_author",
                    "is_article_editor",
                    "is_case_editor",
                    "about_me",
                    "en_name",

                    "hx_cc_ai_permission",
                    "hx_cc_ai_use_count",

                    "hx_pi_ai_permission",
                    "hx_pi_ai_use_count",
                )
            },
        ),
    )

    list_display_links = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)

