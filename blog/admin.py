#coding:utf-8

from django.contrib import admin
from blog.models import Author,Blog,Tag

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','email',)
    search_fields = ('name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','publish_time')
    ordering = ('-publish_time',)
    date_hierarchy = 'publish_time'
    filter_horizontal = ('tags',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Blog,BlogAdmin)
