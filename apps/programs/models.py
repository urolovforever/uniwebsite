from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.core.translation import TranslatedMixin


class Department(TranslatedMixin, models.Model):
    name = models.CharField(max_length=200)
    name_uz = models.CharField(max_length=200, blank=True)
    name_ru = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = CKEditor5Field(blank=True, config_name='default')
    description_uz = CKEditor5Field(blank=True, config_name='default')
    description_ru = CKEditor5Field(blank=True, config_name='default')
    image = models.ImageField(upload_to='departments/', blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('programs:department_detail', kwargs={'slug': self.slug})


class Program(TranslatedMixin, models.Model):
    LEVEL_CHOICES = [
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD'),
    ]
    STUDY_TYPE_CHOICES = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
    ]

    title = models.CharField(max_length=300)
    title_uz = models.CharField(max_length=300, blank=True)
    title_ru = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    study_type = models.CharField(max_length=20, choices=STUDY_TYPE_CHOICES, default='full-time')
    language = models.CharField(max_length=50, default='English')
    tuition_fee = models.CharField(max_length=100, blank=True, help_text='e.g. "22,000,000 UZS"')
    description = CKEditor5Field(blank=True, config_name='default')
    description_uz = CKEditor5Field(blank=True, config_name='default')
    description_ru = CKEditor5Field(blank=True, config_name='default')
    duration = models.CharField(max_length=100, blank=True, help_text='e.g. "4 years"')
    image = models.ImageField(upload_to='programs/', blank=True)
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.get_level_display()})"

    def get_absolute_url(self):
        return reverse('programs:program_detail', kwargs={'slug': self.slug})
