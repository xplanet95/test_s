from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content',)
    list_filter = ('created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, NewsAdmin)
