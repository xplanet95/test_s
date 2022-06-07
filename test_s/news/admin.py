from django.contrib import admin
from .models import News, Category
from django.utils.safestring import mark_safe


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published',
                    'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    #  возможность менять is_published
    list_editable = ('is_published',)
    list_filter = ('created_at', 'updated_at')
    # поля для вывода внутри новости
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'cnt_views',
              'created_at', 'updated_at')
    #  какие поля не редактируемые
    readonly_fields = ('get_photo', 'cnt_views', 'created_at', 'updated_at')
    save_on_top = True

    # Метод что бы получить миниатюру картинки, объект картинки это obj
    def get_photo(self, obj):
        if obj.photo:
            # mark_safe что бы возвращать нормальный html, а не путь к картинке
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            # Дефис по умолчанию
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

# admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'