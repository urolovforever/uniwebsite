import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST
from .models import Category, NewsArticle, Event, PublicationCategory, AuthorType, Publication, GalleryImage, NewsletterSubscriber, EventRegistration


def news_list(request):
    articles = NewsArticle.objects.filter(is_published=True)
    categories = Category.objects.all()
    search_query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '')
    if search_query:
        articles = articles.filter(title__icontains=search_query)
    if selected_category:
        articles = articles.filter(categories__slug=selected_category)
    paginator = Paginator(articles, 12)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'news/news_list.html', {
        'articles': page,
        'categories': categories,
        'search_query': search_query,
        'selected_category': selected_category,
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
    categories = Category.objects.all()
    selected_category = request.GET.get('category', '')
    show_past = request.GET.get('past', '')
    search_query = request.GET.get('q', '').strip()
    if search_query:
        events = events.filter(title__icontains=search_query)
    if selected_category:
        events = events.filter(categories__slug=selected_category)
    if not show_past:
        events = events.filter(event_date__gte=timezone.now().date())
    paginator = Paginator(events, 12)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'news/event_list.html', {
        'events': page,
        'categories': categories,
        'selected_category': selected_category,
        'show_past': show_past,
        'search_query': search_query,
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


def publication_list(request):
    publications = Publication.objects.filter(is_published=True)
    categories = PublicationCategory.objects.all()
    author_types = AuthorType.objects.all()
    search_query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '')
    selected_type = request.GET.get('type', '')
    if search_query:
        publications = publications.filter(title__icontains=search_query)
    if selected_category:
        publications = publications.filter(categories__slug=selected_category)
    if selected_type:
        publications = publications.filter(author_type__slug=selected_type)
    paginator = Paginator(publications, 12)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'news/publication_list.html', {
        'publications': page,
        'categories': categories,
        'author_types': author_types,
        'search_query': search_query,
        'selected_category': selected_category,
        'selected_type': selected_type,
        'hero_title': _('Publications'),
        'hero_category': _('Research & Publications'),
        'hero_description': _('Academic articles and research papers by TIU faculty and students.'),
        'breadcrumbs': [
            {'title': _('News'), 'url': reverse('news:news_list')},
            {'title': _('Publications'), 'url': None},
        ],
    })


def publication_detail(request, slug):
    publication = get_object_or_404(Publication, slug=slug, is_published=True)
    related = Publication.objects.filter(is_published=True).exclude(pk=publication.pk)[:5]
    return render(request, 'news/publication_detail.html', {
        'publication': publication,
        'related_publications': related,
        'hero_title': publication.t('title'),
        'hero_category': _('Publications'),
        'hero_description': publication.t('excerpt') or '',
        'breadcrumbs': [
            {'title': _('News'), 'url': reverse('news:news_list')},
            {'title': _('Publications'), 'url': reverse('news:publications')},
            {'title': publication.t('title'), 'url': None},
        ],
    })


def gallery(request):
    images_qs = GalleryImage.objects.all()
    paginator = Paginator(images_qs, 24)
    images = paginator.get_page(request.GET.get('page'))
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
