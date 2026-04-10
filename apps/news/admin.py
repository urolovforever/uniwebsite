from django.contrib import admin
from .models import Category, NewsArticle, Event, PublicationCategory, AuthorType, Publication, GalleryImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_uz', 'name_ru', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'name_uz', 'name_ru']


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'faculty', 'published_date', 'is_published']
    list_filter = ['is_published', 'faculty', 'categories']
    search_fields = ['title', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    exclude = ['is_featured', 'is_top']
    filter_horizontal = ['categories']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'faculty', 'event_date', 'event_time', 'is_published']
    list_filter = ['is_published', 'faculty', 'categories']
    search_fields = ['title', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['is_featured', 'is_top']
    filter_horizontal = ['categories']


@admin.register(PublicationCategory)
class PublicationCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_uz', 'name_ru', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'name_uz', 'name_ru']


@admin.register(AuthorType)
class AuthorTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_uz', 'name_ru', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'name_uz', 'name_ru']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'person', 'author_type', 'published_date', 'is_published']
    list_filter = ['is_published', 'author_type', 'categories', 'person']
    search_fields = ['title', 'author', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    filter_horizontal = ['categories']
    autocomplete_fields = ['person']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'order', 'created_at']
    list_editable = ['order']




