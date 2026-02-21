import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST
from .models import NewsArticle, Event, PressRelease, GalleryImage, NewsletterSubscriber, EventRegistration


def news_list(request):
    articles = NewsArticle.objects.filter(is_published=True)
    search_query = request.GET.get('q', '').strip()
    featured_only = request.GET.get('featured', '')
    if search_query:
        articles = articles.filter(title__icontains=search_query)
    if featured_only:
        articles = articles.filter(is_featured=True)
    paginator = Paginator(articles, 12)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'news/news_list.html', {
        'articles': page,
        'search_query': search_query,
        'featured_only': featured_only,
        'hero_title': _('News'),
        'hero_category': _('News & Media'),
        'hero_description': _('Stay informed with the latest news, announcements, and stories from Tashkent International University.'),
        'breadcrumbs': [{'title': _('News'), 'url': None}],
    })


def news_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug, is_published=True)
    related_articles = NewsArticle.objects.filter(is_published=True).exclude(pk=article.pk)[:5]
    return render(request, 'news/news_detail.html', {
        'article': article,
        'related_articles': related_articles,
        'hero_title': article.t('title'),
        'hero_category': _('News'),
        'hero_description': article.t('excerpt') or '',
        'breadcrumbs': [
            {'title': _('News'), 'url': reverse('news:news_list')},
            {'title': article.t('title'), 'url': None},
        ],
    })


def event_list(request):
    events = Event.objects.filter(is_published=True)
    categories = Event.objects.filter(is_published=True).exclude(category='').values_list('category', flat=True).distinct()
    selected_category = request.GET.get('category', '')
    show_past = request.GET.get('past', '')
    if selected_category:
        events = events.filter(category=selected_category)
    if not show_past:
        events = events.filter(event_date__gte=timezone.now().date())
    paginator = Paginator(events, 12)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'news/event_list.html', {
        'events': page,
        'categories': categories,
        'selected_category': selected_category,
        'show_past': show_past,
        'hero_title': _('Events'),
        'hero_category': _('News & Media'),
        'hero_description': _('Discover upcoming events, workshops, conferences, and activities happening at TIU.'),
        'breadcrumbs': [
            {'title': _('News'), 'url': reverse('news:news_list')},
            {'title': _('Events'), 'url': None},
        ],
    })


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug, is_published=True)
    upcoming_events = Event.objects.filter(
        is_published=True, event_date__gte=timezone.now().date()
    ).exclude(pk=event.pk)[:5]
    return render(request, 'news/event_detail.html', {
        'event': event,
        'upcoming_events': upcoming_events,
        'hero_title': event.t('title'),
        'hero_category': _('Events'),
        'breadcrumbs': [
            {'title': _('News'), 'url': reverse('news:news_list')},
            {'title': _('Events'), 'url': reverse('news:event_list')},
            {'title': event.t('title'), 'url': None},
        ],
    })


def press_list(request):
    releases = PressRelease.objects.filter(is_published=True)
    search_query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '')
    if search_query:
        releases = releases.filter(title__icontains=search_query)
    if selected_category:
        releases = releases.filter(category=selected_category)
    categories = PressRelease.CATEGORY_CHOICES
    paginator = Paginator(releases, 12)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'news/press_list.html', {
        'releases': page,
        'search_query': search_query,
        'selected_category': selected_category,
        'categories': categories,
        'hero_title': _('Press Releases'),
        'hero_category': _('News & Media'),
        'hero_description': _('Official statements, announcements, and media resources from Tashkent International University.'),
        'breadcrumbs': [
            {'title': _('News'), 'url': reverse('news:news_list')},
            {'title': _('Press Releases'), 'url': None},
        ],
    })


def press_detail(request, slug):
    release = get_object_or_404(PressRelease, slug=slug, is_published=True)
    related_releases = PressRelease.objects.filter(is_published=True).exclude(pk=release.pk)[:5]
    return render(request, 'news/press_detail.html', {
        'release': release,
        'related_releases': related_releases,
        'hero_title': release.t('title'),
        'hero_category': _('Press Releases'),
        'hero_description': release.t('excerpt') or '',
        'breadcrumbs': [
            {'title': _('News'), 'url': reverse('news:news_list')},
            {'title': _('Press'), 'url': reverse('news:press_releases')},
            {'title': release.t('title'), 'url': None},
        ],
    })


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'news/gallery.html', {
        'images': images,
        'hero_title': _('Gallery'),
        'hero_category': _('News & Media'),
        'hero_description': _('Browse photos from campus life, events, and academic activities at Tashkent International University.'),
        'breadcrumbs': [
            {'title': _('News'), 'url': reverse('news:news_list')},
            {'title': _('Gallery'), 'url': None},
        ],
    })


@require_POST
def newsletter_subscribe(request):
    """API endpoint for newsletter subscription."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': _('Invalid request.')}, status=400)

    email = data.get('email', '').strip().lower()
    if not email or '@' not in email:
        return JsonResponse({'success': False, 'message': _('Please enter a valid email address.')}, status=400)

    subscriber, created = NewsletterSubscriber.objects.get_or_create(
        email=email,
        defaults={'is_active': True},
    )
    if not created:
        if subscriber.is_active:
            return JsonResponse({'success': False, 'message': _('This email is already subscribed.')})
        subscriber.is_active = True
        subscriber.save(update_fields=['is_active'])

    return JsonResponse({'success': True, 'message': _('Successfully subscribed to our newsletter!')})


@require_POST
def event_register(request):
    """API endpoint for event registration."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': _('Invalid request.')}, status=400)

    event_id = data.get('event_id')
    name = data.get('name', '').strip()
    email = data.get('email', '').strip().lower()

    if not name:
        return JsonResponse({'success': False, 'message': _('Please enter your name.')}, status=400)
    if not email or '@' not in email:
        return JsonResponse({'success': False, 'message': _('Please enter a valid email address.')}, status=400)

    event = get_object_or_404(Event, pk=event_id, is_published=True)

    _, created = EventRegistration.objects.get_or_create(
        event=event,
        email=email,
        defaults={'name': name},
    )
    if not created:
        return JsonResponse({'success': False, 'message': _('You are already registered for this event.')})

    return JsonResponse({'success': True, 'message': _('Successfully registered for the event!')})
