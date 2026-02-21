from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.news.models import NewsArticle, Event
from apps.programs.models import Program, Department


class StaticPagesSitemap(Sitemap):
    """Sitemap for all static pages."""
    i18n = True
    changefreq = 'monthly'
    priority = 0.6

    STATIC_PAGES = [
        # About
        'about/overview', 'about/mission-vision', 'about/leadership',
        'about/why-tiu', 'about/sustainability', 'about/campus-map',
        # Admissions
        'admissions/how-to-apply', 'admissions/requirements',
        'admissions/tuition-fees', 'admissions/scholarships',
        'admissions/apply-now', 'admissions/apply-bachelor',
        'admissions/apply-master', 'admissions/apply-international',
        'admissions/faqs',
        # Programs
        'programs/by-faculty', 'programs/by-level',
        'programs/international-programs', 'programs/joint-degrees',
        'programs/exchange-programs', 'programs/dual-diploma',
        # Current Students
        'current-students/academic-life', 'current-students/timetable',
        'current-students/exams-results', 'current-students/library',
        'current-students/lms', 'current-students/housing',
        'current-students/cafeteria', 'current-students/sports',
        'current-students/clubs', 'current-students/student-union',
        'current-students/campus-services', 'current-students/it-services',
        'current-students/registration', 'current-students/calendar',
        'current-students/student-life',
        # International
        'international/why-study-tiu', 'international/admission-process',
        'international/visa-immigration', 'international/accommodation',
        'international/partner-universities', 'international/exchange-opportunities',
        # Research
        'research/centers', 'research/publications',
        'research/conferences', 'research/innovation',
        # Careers
        'careers/career-center', 'careers/internships',
        'careers/employer-partnerships', 'careers/alumni-network',
        # Contact
        'contact/contact-info', 'contact/rector-reception', 'contact/support',
        # Faculty
        'faculty/departments', 'faculty/directory', 'faculty/profiles',
        # Legal
        'privacy-policy', 'terms-of-use',
    ]

    def items(self):
        return self.STATIC_PAGES

    def location(self, item):
        return f'/{item}/'


class HomepageSitemap(Sitemap):
    i18n = True
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return ['homepage']

    def location(self, item):
        return '/'


class NewsSitemap(Sitemap):
    i18n = True
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return NewsArticle.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.published_date

    def location(self, obj):
        return obj.get_absolute_url()


class EventsSitemap(Sitemap):
    i18n = True
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Event.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('news:event_detail', kwargs={'slug': obj.slug})


class ProgramsSitemap(Sitemap):
    i18n = True
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Program.objects.filter(is_published=True)

    def location(self, obj):
        return obj.get_absolute_url()


class DepartmentsSitemap(Sitemap):
    i18n = True
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Department.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()
