from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.core.translation import TranslatedMixin


class Leader(TranslatedMixin, models.Model):
    CATEGORY_CHOICES = [
        ('rektorat', 'Rektorat'),
        ('departament', 'Departament'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200)
    job_title_uz = models.CharField(max_length=200, blank=True)
    job_title_ru = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='rektorat')
    photo = models.ImageField(upload_to='leadership/', blank=True)
    excerpt = models.TextField(blank=True, help_text='Short intro shown by default')
    excerpt_uz = models.TextField(blank=True)
    excerpt_ru = models.TextField(blank=True)
    bio = CKEditor5Field(blank=True, config_name='default', help_text='Full bio shown when "Find out more" is clicked')
    bio_uz = CKEditor5Field(blank=True, config_name='default')
    bio_ru = CKEditor5Field(blank=True, config_name='default')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Leader'
        verbose_name_plural = 'Leadership'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Person(TranslatedMixin, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    job_title = models.CharField(max_length=200)
    job_title_uz = models.CharField(max_length=200, blank=True)
    job_title_ru = models.CharField(max_length=200, blank=True)
    department = models.ForeignKey(
        'programs.Department', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='people'
    )
    photo = models.ImageField(upload_to='people/', blank=True)
    bio = CKEditor5Field(blank=True, config_name='default')
    bio_uz = CKEditor5Field(blank=True, config_name='default')
    bio_ru = CKEditor5Field(blank=True, config_name='default')
    email = models.EmailField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'last_name']
        verbose_name = 'Faculty & Staff'
        verbose_name_plural = 'Faculty & Staff'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('people:person_detail', kwargs={'slug': self.slug})
