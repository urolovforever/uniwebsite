from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.core.translation import TranslatedMixin


class Category(TranslatedMixin, models.Model):
    name = models.CharField(max_length=100)
    name_uz = models.CharField(max_length=100, blank=True)
    name_ru = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class NewsArticle(TranslatedMixin, models.Model):
    FACULTY_CHOICES = [
        ('jurisprudence', 'Faculty of Jurisprudence'),
        ('business', 'Faculty of Business and Innovative Education'),
    ]
    title = models.CharField(max_length=300)
    title_uz = models.CharField(max_length=300, blank=True)
    title_ru = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    faculty = models.CharField(max_length=50, choices=FACULTY_CHOICES, blank=True)
    excerpt = models.TextField(blank=True)
    excerpt_uz = models.TextField(blank=True)
    excerpt_ru = models.TextField(blank=True)
    body = CKEditor5Field(config_name='default')
    body_uz = CKEditor5Field(blank=True, config_name='default')
    body_ru = CKEditor5Field(blank=True, config_name='default')
    featured_image = models.ImageField(upload_to='news/', blank=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='news_articles')
    is_featured = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news_detail', kwargs={'slug': self.slug})


class Event(TranslatedMixin, models.Model):
    FACULTY_CHOICES = [
        ('jurisprudence', 'Faculty of Jurisprudence'),
        ('business', 'Faculty of Business and Innovative Education'),
    ]
    title = models.CharField(max_length=300)
    title_uz = models.CharField(max_length=300, blank=True)
    title_ru = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    faculty = models.CharField(max_length=50, choices=FACULTY_CHOICES, blank=True)
    excerpt = models.TextField(blank=True)
    excerpt_uz = models.TextField(blank=True)
    excerpt_ru = models.TextField(blank=True)
    description = CKEditor5Field(config_name='default')
    description_uz = CKEditor5Field(blank=True, config_name='default')
    description_ru = CKEditor5Field(blank=True, config_name='default')
    image = models.ImageField(upload_to='events/', blank=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='events')
    event_date = models.DateField()
    event_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=300, blank=True)
    is_featured = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:event_detail', kwargs={'slug': self.slug})


class PublicationCategory(TranslatedMixin, models.Model):
    name = models.CharField(max_length=100)
    name_uz = models.CharField(max_length=100, blank=True)
    name_ru = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Publication Categories'

    def __str__(self):
        return self.name


class AuthorType(TranslatedMixin, models.Model):
    name = models.CharField(max_length=100)
    name_uz = models.CharField(max_length=100, blank=True)
    name_ru = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Publication(TranslatedMixin, models.Model):
    title = models.CharField(max_length=300)
    title_uz = models.CharField(max_length=300, blank=True)
    title_ru = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.CharField(max_length=300)
    author_type = models.ForeignKey(AuthorType, on_delete=models.SET_NULL, null=True, blank=True)
    person = models.ForeignKey(
        'people.Person', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='publications',
        help_text='Link to a faculty member (optional)'
    )
    excerpt = models.TextField(blank=True)
    excerpt_uz = models.TextField(blank=True)
    excerpt_ru = models.TextField(blank=True)
    body = CKEditor5Field(blank=True, config_name='default')
    body_uz = CKEditor5Field(blank=True, config_name='default')
    body_ru = CKEditor5Field(blank=True, config_name='default')
    featured_image = models.ImageField(upload_to='publications/', blank=True)
    external_url = models.URLField(blank=True, help_text='Link to external publication (journal, conference, etc.)')
    categories = models.ManyToManyField(PublicationCategory, blank=True, related_name='publications')
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:publication_detail', kwargs={'slug': self.slug})


class GalleryImage(TranslatedMixin, models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=300, blank=True)
    caption_uz = models.CharField(max_length=300, blank=True)
    caption_ru = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.caption or f'Image #{self.pk}'


class NewsletterSubscriber(models.Model):
    """Email newsletter subscriptions."""
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-subscribed_at']

    def __str__(self):
        return self.email


class EventRegistration(models.Model):
    """Event attendance registrations."""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-registered_at']
        unique_together = ['event', 'email']

    def __str__(self):
        return f'{self.name} — {self.event.title}'
