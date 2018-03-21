from django.contrib import admin
from ratemy.models import Category, Post


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'picture', 'likes')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'followers')
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PageAdmin)