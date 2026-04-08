from django.contrib import admin
from .models import JobDepartment, JobType, JobRole, JobPosition


@admin.register(JobDepartment)
class JobDepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_uz', 'name_ru']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_uz', 'name_ru']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_uz', 'name_ru']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'job_type', 'role', 'salary', 'deadline', 'is_active']
    list_filter = ['department', 'job_type', 'role', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {'fields': ('title', 'title_uz', 'title_ru', 'slug')}),
        ('Details', {'fields': ('department', 'job_type', 'role', 'deadline', 'is_active')}),
        ('Salary', {'fields': ('salary', 'salary_uz', 'salary_ru')}),
        ('Description (English)', {'fields': ('description',)}),
        ('Description (Uzbek)', {'fields': ('description_uz',), 'classes': ('collapse',)}),
        ('Description (Russian)', {'fields': ('description_ru',), 'classes': ('collapse',)}),
    )
