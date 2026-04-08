from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.core.translation import TranslatedMixin


class JobDepartment(TranslatedMixin, models.Model):
    name = models.CharField(max_length=200)
    name_uz = models.CharField(max_length=200, blank=True)
    name_ru = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class JobType(TranslatedMixin, models.Model):
    name = models.CharField(max_length=100)
    name_uz = models.CharField(max_length=100, blank=True)
    name_ru = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Job Type'
        verbose_name_plural = 'Job Types'

    def __str__(self):
        return self.name


class JobRole(TranslatedMixin, models.Model):
    name = models.CharField(max_length=100)
    name_uz = models.CharField(max_length=100, blank=True)
    name_ru = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name


class JobPosition(TranslatedMixin, models.Model):
    title = models.CharField(max_length=200)
    title_uz = models.CharField(max_length=200, blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    department = models.ForeignKey(JobDepartment, on_delete=models.SET_NULL, null=True, blank=True)
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(JobRole, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.CharField(max_length=200, blank=True, help_text='e.g. "5,000,000 - 8,000,000 UZS" or "Discussed at interview"')
    salary_uz = models.CharField(max_length=200, blank=True)
    salary_ru = models.CharField(max_length=200, blank=True)
    deadline = models.DateField()
    description = CKEditor5Field(blank=True, config_name='default')
    description_uz = CKEditor5Field(blank=True, config_name='default')
    description_ru = CKEditor5Field(blank=True, config_name='default')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:job_detail', kwargs={'slug': self.slug})
