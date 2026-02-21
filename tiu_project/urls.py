from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView, TemplateView
from django.contrib.sitemaps.views import sitemap

from apps.core.sitemaps import (
    HomepageSitemap,
    StaticPagesSitemap,
    NewsSitemap,
    EventsSitemap,
    ProgramsSitemap,
    DepartmentsSitemap,
)

sitemaps = {
    'homepage': HomepageSitemap,
    'static': StaticPagesSitemap,
    'news': NewsSitemap,
    'events': EventsSitemap,
    'programs': ProgramsSitemap,
    'departments': DepartmentsSitemap,
}

# URLs that should NOT be language-prefixed
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    # SEO
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

# URLs that ARE language-prefixed (/en/, /uz/, /ru/)
urlpatterns += i18n_patterns(
    # Redirects
    path('international/dual-degree/', RedirectView.as_view(url='/programs/dual-diploma/', permanent=True)),
    # Dynamic apps
    path('news/', include('apps.news.urls')),
    path('programs/', include('apps.programs.urls')),
    path('faculty/', include('apps.people.urls')),
    # Homepage + static page catch-all — must be last
    path('', include('apps.core.urls')),
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
