from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "reporter", "date_posted", "category", "status"]
    list_editable = ["category", "status"]
    list_filter = ["category", "reporter"]
    prepopulated_fields = {"slug": ('category', 'title',)}

admin.site.register(News, NewsAdmin)
