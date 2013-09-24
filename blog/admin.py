#-*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Category, Article, Contact


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'content_peek')
    list_filter = ('author', 'category')
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title', ), }
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Metadata', {
            'classes': ['collpase', ],
            'fields': ('title', 'slug', 'author', 'category')
        }),
        # Fieldset 2 : contenu de l'article
        ('Article content', {
            'description': u'HTML can be used (don\'t break anything)',
            'classes': ['extrapretty', ],
            'fields': ('content', )
        }),
    )

    def content_peek(self, article):
        """
        Return the content shortened to 40 characters
        """
        text = article.content[0:40]
        if len(article.content) > 40:
            return '%s...' % text
        else:
            return text


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact)
