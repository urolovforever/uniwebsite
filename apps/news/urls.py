from django.urls import path
from . import views
from .feeds import LatestNewsFeed

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('events/', views.event_list, name='event_list'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('publications/', views.publication_list, name='publications'),
    path('publications/<slug:slug>/', views.publication_detail, name='publication_detail'),
    path('feed/', LatestNewsFeed(), name='news_feed'),
    path('api/newsletter-subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('api/event-register/', views.event_register, name='event_register'),
    path('<slug:slug>/', views.news_detail, name='news_detail'),
]
