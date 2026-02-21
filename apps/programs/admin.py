from django.contrib import admin
from .models import Department, Program


class ProgramInline(admin.TabularInline):
    model = Program
    extra = 0
    fields = ['title', 'level', 'study_type', 'duration', 'tuition_fee', 'slug', 'order', 'is_published']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProgramInline]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'level', 'study_type', 'tuition_fee', 'duration', 'is_published', 'order']
    list_filter = ['department', 'level', 'study_type', 'is_published']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order']
