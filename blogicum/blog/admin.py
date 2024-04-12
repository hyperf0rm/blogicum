from django.contrib import admin
from .models import Category, Location, Post, Comment

# Register your models here.

admin.site.empty_value_display = 'Не задано'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'is_published',
        'created_at',
        'author',
        'category',
        'location'
    )
    list_editable = (
        'is_published',
        'pub_date',
        'category',
        'location'
    )
    search_fields = ('title',)
    list_filter = ('category',)


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = (
        'slug',
        'is_published'
    )
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Comment)
