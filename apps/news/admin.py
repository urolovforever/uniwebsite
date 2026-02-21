from django.contrib import admin
from .models import NewsArticle, Event, PressRelease, GalleryImage, NewsletterSubscriber, EventRegistration


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'is_featured', 'is_top', 'is_published']
    list_filter = ['is_published', 'is_featured', 'is_top']
    search_fields = ['title', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'event_time', 'category', 'is_featured', 'is_top', 'is_published']
    list_filter = ['is_published', 'is_featured', 'is_top', 'category']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'category', 'is_published']
    list_filter = ['is_published', 'category']
    search_fields = ['title', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'order', 'created_at']
    list_editable = ['order']


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'subscribed_at']
    list_filter = ['is_active']
    search_fields = ['email']
    date_hierarchy = 'subscribed_at'


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'event', 'registered_at']
    list_filter = ['event']
    search_fields = ['name', 'email']
    date_hierarchy = 'registered_at'
