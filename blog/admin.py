from django.contrib import admin
from blog.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'category')
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('title', 'content')


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
