from django.contrib import admin
from .models import Leader, Person


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'job_title', 'category', 'order']
    list_filter = ['category']
    list_editable = ['order']
    search_fields = ['first_name', 'last_name', 'job_title']
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'photo', 'category')}),
        ('Title', {'fields': ('job_title', 'job_title_uz', 'job_title_ru')}),
        ('Excerpt', {'fields': ('excerpt', 'excerpt_uz', 'excerpt_ru')}),
        ('Full Bio (English)', {'fields': ('bio',)}),
        ('Full Bio (Uzbek)', {'fields': ('bio_uz',), 'classes': ('collapse',)}),
        ('Full Bio (Russian)', {'fields': ('bio_ru',), 'classes': ('collapse',)}),
        ('Other', {'fields': ('order',)}),
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'job_title', 'department', 'order']
    list_filter = ['department']
    search_fields = ['first_name', 'last_name', 'job_title']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_editable = ['order']
