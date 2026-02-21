from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import NewsArticle


class LatestNewsFeed(Feed):
    title = 'TIU News'
    link = reverse_lazy('news:news_list')
    description = 'Latest news and announcements from Tashkent International University.'

    def items(self):
        return NewsArticle.objects.filter(is_published=True)[:20]

    def item_title(self, item):
        return item.t('title')

    def item_description(self, item):
        return item.t('excerpt')

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.published_date
