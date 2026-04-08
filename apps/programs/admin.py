from django.contrib import admin
from .models import Department, Program


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'order']
    list_filter = ['faculty']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'faculty', 'level', 'study_type', 'tuition_fee', 'duration', 'is_published', 'order']
    list_filter = ['faculty', 'level', 'study_type', 'is_published']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order']
