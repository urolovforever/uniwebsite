from django import template
from django.utils import timezone

from apps.news.models import NewsArticle, Event

register = template.Library()


@register.inclusion_tag('news/includes/latest_news_list.html')
def latest_news(count=3):
    articles = NewsArticle.objects.filter(is_published=True)[:count]
    return {'articles': articles}


@register.inclusion_tag('news/includes/upcoming_events_list.html')
def upcoming_events(count=2):
    today = timezone.now().date()
    events = Event.objects.filter(is_published=True, event_date__gte=today)[:count]
    return {'events': events}
