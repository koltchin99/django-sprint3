from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'description',
                'slug',
            )
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',),
            'fields': (
                'is_published',
            ),
        }),
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',),
            'fields': (
                'is_published',
            ),
        }),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'location')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'
    filter_horizontal = ()

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'text',
                'author',
                'location',
                'category',
            )
        }),
        ('Публикация', {
            'fields': (
                'pub_date',
                'is_published',
            )
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',),
            'fields': (),
        }),
    )
