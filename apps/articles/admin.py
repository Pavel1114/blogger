from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.articles.models import Article


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ("__str__", "created", "author")
    search_fields = ["title", "text"]

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)
