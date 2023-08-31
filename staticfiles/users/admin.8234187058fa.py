from django.contrib import admin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", 'date_joined', ]
    list_filter = ["last_name",]


admin.site.register(CustomUser, CustomUserAdmin)
