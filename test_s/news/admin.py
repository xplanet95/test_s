from django.contrib import admin
from .models import News, Category
from django.utils.safestring import mark_safe


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    #  возможность менять is_published
    list_editable = ('is_published',)
    list_filter = ('created_at', 'updated_at')
    # fields = ('id', 'title', 'category', 'content', 'photo', 'get_photo', 'is_published')
    #  какие поля не редактируемые
    # readonly_fields = ('views', 'created_at', 'updated_at',)

    # Метод что бы получить миниатюру картинки, объект картинки это obj
    def get_photo(self, obj):
        if obj.photo:
            # mark_safe что бы возвращать нормальный html, а не путь к картинке
            return mark_safe(f'<img scr="{obj.photo.url}" width="75">')
        else:
            return '-'
    #  Название поля в админке
    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    #  ?
    empty_value_display = 'без категории'


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
