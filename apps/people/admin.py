from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role', 'job_title', 'department', 'order']
    list_filter = ['role', 'department']
    search_fields = ['first_name', 'last_name', 'job_title']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_editable = ['order']
