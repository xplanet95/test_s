from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'content')
    search_fields = ('title', 'content',)
    list_filter = ('created_at', 'updated_at')


admin.site.register(News, NewsAdmin)
