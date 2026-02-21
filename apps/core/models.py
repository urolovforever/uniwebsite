from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.core.translation import TranslatedMixin


class SiteSettings(TranslatedMixin, models.Model):
    """Singleton model for global site settings."""
    site_name = models.CharField(max_length=200, default='Tashkent International University')
    site_name_uz = models.CharField(max_length=200, blank=True)
    site_name_ru = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='site/', blank=True)
    # Contact info
    address = models.CharField(max_length=300, default='Tashkent, Uzbekistan')
    address_uz = models.CharField(max_length=300, blank=True)
    address_ru = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=50, default='+998 71 XXX XX XX')
    email = models.EmailField(default='info@tiu.uz')
    # Social media
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    telegram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    # Analytics
    google_analytics_id = models.CharField(
        max_length=30, blank=True,
        help_text='Google Analytics Measurement ID (e.g. G-XXXXXXXXXX)',
    )

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ContactMessage(models.Model):
    """Stores contact form submissions."""
    TOPIC_CHOICES = [
        ('admissions', 'Admissions'),
        ('academics', 'Academics'),
        ('financial', 'Tuition & Financial Aid'),
        ('international', 'International Students'),
        ('careers', 'Career Services'),
        ('it', 'IT Support'),
        ('general', 'General Inquiry'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'{self.name} — {self.get_topic_display()} ({self.created_at:%Y-%m-%d})'


class Partner(models.Model):
    """Partner university logos for carousel."""
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/')
    website_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class JobPosition(TranslatedMixin, models.Model):
    """Open job positions displayed on the careers/hiring page."""
    DEPARTMENT_CHOICES = [
        ('it', 'School of IT & Engineering'),
        ('business', 'School of Business & Economics'),
        ('law', 'School of Law'),
        ('humanities', 'School of Humanities & Social Sciences'),
        ('foundation', 'Foundation Programme'),
        ('admin', 'Administrative'),
    ]
    JOB_TYPE_CHOICES = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
    ]
    ROLE_CHOICES = [
        ('academic', 'Academic'),
        ('staff', 'Staff'),
    ]

    title = models.CharField(max_length=200)
    title_uz = models.CharField(max_length=200, blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    department_label = models.CharField(
        max_length=100, blank=True,
        help_text='Display name for the department (e.g. "Information Technology Department"). Leave blank to use default.',
    )
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
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

    @property
    def display_department(self):
        return self.department_label or self.get_department_display()


class Scholarship(TranslatedMixin, models.Model):
    """Scholarships displayed on the admissions/scholarships page."""
    LEVEL_CHOICES = [
        ('bachelor', "Bachelor's"),
        ('master', "Master's"),
        ('bachelor master', "Bachelor's & Master's"),
        ('all-levels', 'All levels'),
    ]
    TYPE_CHOICES = [
        ('merit', 'Merit-based'),
        ('need', 'Need-based'),
        ('special', 'Special category'),
    ]
    APPLICANT_CHOICES = [
        ('domestic', 'Domestic'),
        ('international', 'International'),
        ('domestic international', 'Domestic & International'),
    ]
    TAG_COLOR_CHOICES = [
        ('tag-gold', 'Gold'),
        ('tag-green', 'Green'),
        ('tag-purple', 'Purple'),
    ]
    TAG_ICON_CHOICES = [
        ('fas fa-trophy', 'Trophy'),
        ('fas fa-percent', 'Percent'),
        ('fas fa-hand-holding-usd', 'Hand holding USD'),
    ]

    title = models.CharField(max_length=200)
    title_uz = models.CharField(max_length=200, blank=True)
    title_ru = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    provider = models.CharField(max_length=200, default='Tashkent International University')
    excerpt = models.TextField(help_text='Short description shown on the list page')
    excerpt_uz = models.TextField(blank=True)
    excerpt_ru = models.TextField(blank=True)
    description = CKEditor5Field(blank=True, config_name='default')
    description_uz = CKEditor5Field(blank=True, config_name='default')
    description_ru = CKEditor5Field(blank=True, config_name='default')
    level = models.CharField(max_length=30, choices=LEVEL_CHOICES)
    award_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    applicant_type = models.CharField(max_length=30, choices=APPLICANT_CHOICES)
    award_tag_text = models.CharField(
        max_length=100,
        help_text='e.g. "Full Fee Waiver", "50% Tuition Discount"',
    )
    award_tag_color = models.CharField(max_length=20, choices=TAG_COLOR_CHOICES, default='tag-green')
    award_tag_icon = models.CharField(max_length=50, choices=TAG_ICON_CHOICES, default='fas fa-percent')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:scholarship_detail', kwargs={'slug': self.slug})

    @property
    def type_tag_color(self):
        return {'merit': 'tag-blue', 'need': 'tag-pink', 'special': 'tag-orange'}.get(self.award_type, 'tag-blue')

    @property
    def type_tag_icon(self):
        return {'merit': 'fas fa-list-alt', 'need': 'fas fa-list-alt', 'special': 'fas fa-star'}.get(self.award_type, 'fas fa-list-alt')

    @property
    def is_international_only(self):
        return self.applicant_type == 'international'
