from django.contrib import admin
from .models import SiteSettings, Partner, ContactMessage, JobPosition, Scholarship


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('site_name', 'site_name_uz', 'site_name_ru', 'logo')}),
        ('Contact', {'fields': ('address', 'address_uz', 'address_ru', 'phone', 'email')}),
        ('Social Media', {'fields': (
            'facebook_url', 'instagram_url', 'telegram_url',
            'linkedin_url', 'youtube_url', 'twitter_url',
        )}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'topic', 'is_read', 'created_at']
    list_filter = ['topic', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'topic', 'message', 'created_at']
    list_editable = ['is_read']
    date_hierarchy = 'created_at'

    def has_add_permission(self, request):
        return False


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'job_type', 'role', 'deadline', 'is_active']
    list_filter = ['department', 'job_type', 'role', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {'fields': ('title', 'title_uz', 'title_ru', 'slug')}),
        ('Details', {'fields': ('department', 'department_label', 'job_type', 'role', 'deadline', 'is_active')}),
        ('Description (English)', {'fields': ('description',)}),
        ('Description (Uzbek)', {'fields': ('description_uz',), 'classes': ('collapse',)}),
        ('Description (Russian)', {'fields': ('description_ru',), 'classes': ('collapse',)}),
    )


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ['title', 'award_type', 'level', 'applicant_type', 'order', 'is_active']
    list_filter = ['award_type', 'level', 'applicant_type', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {'fields': ('title', 'title_uz', 'title_ru', 'slug', 'provider')}),
        ('Excerpt (English)', {'fields': ('excerpt',)}),
        ('Excerpt (Uzbek)', {'fields': ('excerpt_uz',), 'classes': ('collapse',)}),
        ('Excerpt (Russian)', {'fields': ('excerpt_ru',), 'classes': ('collapse',)}),
        ('Description (English)', {'fields': ('description',)}),
        ('Description (Uzbek)', {'fields': ('description_uz',), 'classes': ('collapse',)}),
        ('Description (Russian)', {'fields': ('description_ru',), 'classes': ('collapse',)}),
        ('Classification', {'fields': ('level', 'award_type', 'applicant_type')}),
        ('Display', {'fields': ('award_tag_text', 'award_tag_color', 'award_tag_icon', 'order', 'is_active')}),
    )
