from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """Custome User Admin"""

    list_display = ("username", "email", "gender", "lang", "currency", "superhost")
    list_filter = ("lang", "gender", "superhost")
