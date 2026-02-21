from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.core.translation import TranslatedMixin


class Person(TranslatedMixin, models.Model):
    ROLE_CHOICES = [
        ('leadership', 'Leadership'),
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
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
        verbose_name_plural = 'People'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('people:person_detail', kwargs={'slug': self.slug})
