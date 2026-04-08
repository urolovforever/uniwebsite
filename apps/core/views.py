from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, JsonResponse
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _

from apps.news.models import NewsArticle, Event, Publication
from apps.programs.models import Program, Department
from apps.core.models import Partner, ContactMessage, Scholarship
from apps.jobs.models import JobPosition
from apps.core.forms import ContactForm


def homepage(request):
    # Latest 6 news: first one is the top story, rest are side list
    news_articles = list(NewsArticle.objects.filter(is_published=True).order_by('-published_date')[:7])

    today = timezone.now().date()
    # Latest 7 events: first one is featured, rest are side list
    upcoming_events = list(Event.objects.filter(is_published=True, event_date__gte=today).order_by('event_date')[:7])

    context = {
        'news_articles': news_articles,
        'upcoming_events': upcoming_events,
        'partners': Partner.objects.filter(is_active=True),
    }
    return render(request, 'home/index.html', context)


def contact_page(request):
    """Handle contact form display and submission."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                topic=form.cleaned_data['topic'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, _('Your message has been sent. We will get back to you shortly.'))
            return redirect('core:contact')
    else:
        form = ContactForm()

    return render(request, 'pages/contact/contact.html', {'form': form})


def site_search(request):
    """Global search across news, events, publications, and programs."""
    query = request.GET.get('q', '').strip()
    results = {'news': [], 'events': [], 'publications': [], 'programs': []}
    total = 0

    if query and len(query) >= 2:
        results['news'] = list(NewsArticle.objects.filter(
            Q(title__icontains=query) | Q(excerpt__icontains=query) |
            Q(title_uz__icontains=query) | Q(title_ru__icontains=query) |
            Q(excerpt_uz__icontains=query) | Q(excerpt_ru__icontains=query),
            is_published=True,
        )[:10])
        results['events'] = list(Event.objects.filter(
            Q(title__icontains=query) | Q(location__icontains=query) |
            Q(title_uz__icontains=query) | Q(title_ru__icontains=query),
            is_published=True,
        )[:10])
        results['publications'] = list(Publication.objects.filter(
            Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(author__icontains=query) |
            Q(title_uz__icontains=query) | Q(title_ru__icontains=query) |
            Q(excerpt_uz__icontains=query) | Q(excerpt_ru__icontains=query),
            is_published=True,
        )[:10])
        results['programs'] = list(Program.objects.filter(
            Q(title__icontains=query) | Q(department__name__icontains=query) |
            Q(title_uz__icontains=query) | Q(title_ru__icontains=query) |
            Q(department__name_uz__icontains=query) | Q(department__name_ru__icontains=query),
            is_published=True,
        ).select_related('department')[:10])
        total = sum(len(v) for v in results.values())

    return render(request, 'pages/search-results.html', {
        'query': query,
        'results': results,
        'total': total,
        'hero_title': _('Search Results'),
        'hero_category': _('Search'),
        'hero_description': _('Found %(total)d results for "%(query)s"') % {'total': total, 'query': query} if query else _('Search across TIU'),
        'breadcrumbs': [{'title': _('Search'), 'url': None}],
    })


def search_api(request):
    """JSON search endpoint for real-time header search."""
    query = request.GET.get('q', '').strip()
    items = []

    if query and len(query) >= 2:
        for article in NewsArticle.objects.filter(
            Q(title__icontains=query) | Q(title_uz__icontains=query) | Q(title_ru__icontains=query),
            is_published=True,
        )[:5]:
            items.append({'title': article.t('title'), 'desc': article.t('excerpt')[:120] if article.t('excerpt') else '', 'url': article.get_absolute_url(), 'type': 'news'})

        for event in Event.objects.filter(
            Q(title__icontains=query) | Q(title_uz__icontains=query) | Q(title_ru__icontains=query),
            is_published=True,
        )[:5]:
            desc = ''
            if event.event_date:
                desc = event.event_date.strftime('%d %b %Y')
                if event.location:
                    desc += ' · ' + event.location
            items.append({'title': event.t('title'), 'desc': desc, 'url': event.get_absolute_url(), 'type': 'event'})

        for pub in Publication.objects.filter(
            Q(title__icontains=query) | Q(title_uz__icontains=query) | Q(title_ru__icontains=query) | Q(author__icontains=query),
            is_published=True,
        )[:5]:
            items.append({'title': pub.t('title'), 'desc': pub.author + ' · ' + (pub.t('excerpt')[:100] if pub.t('excerpt') else ''), 'url': pub.get_absolute_url(), 'type': 'publication'})

        for program in Program.objects.filter(
            Q(title__icontains=query) | Q(title_uz__icontains=query) | Q(title_ru__icontains=query),
            is_published=True,
        ).select_related('department')[:5]:
            desc = program.get_level_display() + ' · ' + program.department.t('name')
            items.append({'title': program.t('title'), 'desc': desc, 'url': program.get_absolute_url(), 'type': 'program'})

    return JsonResponse({'results': items, 'total': len(items)})


def scholarships_page(request):
    """Admissions scholarships page with dynamic scholarship list."""
    scholarships = Scholarship.objects.filter(is_active=True)
    return render(request, 'pages/admissions/scholarships.html', {
        'scholarships': scholarships,
    })


def scholarship_detail(request, slug):
    """Detail page for a single scholarship."""
    scholarship = get_object_or_404(Scholarship, slug=slug, is_active=True)
    other_scholarships = Scholarship.objects.filter(
        is_active=True,
    ).exclude(pk=scholarship.pk)[:5]
    return render(request, 'pages/admissions/scholarship_detail.html', {
        'scholarship': scholarship,
        'other_scholarships': other_scholarships,
        'hero_title': scholarship.t('title'),
        'hero_category': _('Admissions'),
        'hero_description': f'{scholarship.get_award_type_display()} · {scholarship.award_tag_text}',
        'breadcrumbs': [
            {'title': _('Admissions'), 'url': reverse('core:static_page', kwargs={'url_path': 'admissions'})},
            {'title': _('Scholarships'), 'url': reverse('core:scholarships')},
            {'title': scholarship.t('title'), 'url': None},
        ],
    })


def apply_bachelor_page(request):
    """Apply for Bachelor's page with dynamic programme list."""
    programs = Program.objects.filter(
        is_published=True, level='bachelor',
    ).select_related('department')
    return render(request, 'pages/admissions/apply-bachelor.html', {
        'programs': programs,
    })


def apply_master_page(request):
    """Apply for Master's page with dynamic programme list."""
    programs = Program.objects.filter(
        is_published=True, level='master',
    ).select_related('department')
    return render(request, 'pages/admissions/apply-master.html', {
        'programs': programs,
    })


def tuition_fees_page(request):
    """Tuition & Fees page with dynamic fee tables."""
    bachelor_programs = Program.objects.filter(
        is_published=True, level='bachelor',
    ).select_related('department')
    master_programs = Program.objects.filter(
        is_published=True, level='master',
    ).select_related('department')
    phd_programs = Program.objects.filter(
        is_published=True, level='phd',
    ).select_related('department')
    return render(request, 'pages/admissions/tuition-fees.html', {
        'bachelor_programs': bachelor_programs,
        'master_programs': master_programs,
        'phd_programs': phd_programs,
    })


def hiring_page(request):
    """Careers hiring page with dynamic job positions."""
    today = timezone.now().date()
    positions = JobPosition.objects.filter(is_active=True, deadline__gte=today)
    return render(request, 'pages/careers/hiring.html', {
        'positions': positions,
    })


def job_detail(request, slug):
    """Detail page for a single job position."""
    today = timezone.now().date()
    job = get_object_or_404(JobPosition, slug=slug, is_active=True)
    other_positions = JobPosition.objects.filter(
        is_active=True, deadline__gte=today,
    ).exclude(pk=job.pk)[:5]
    return render(request, 'pages/careers/job_detail.html', {
        'job': job,
        'other_positions': other_positions,
        'hero_title': job.t('title'),
        'hero_category': _('Careers'),
        'hero_description': f'{job.department.t("name") if job.department else ""} · {job.job_type.t("name") if job.job_type else ""}',
        'breadcrumbs': [
            {'title': _('Careers'), 'url': reverse('core:static_page', kwargs={'url_path': 'careers'})},
            {'title': _('Open Positions'), 'url': reverse('core:hiring')},
            {'title': job.t('title'), 'url': None},
        ],
    })


def static_page(request, url_path):
    """Serve static content pages by mapping URL path to template file."""
    # Try direct match first, then index.html for section landing pages
    for template_name in [f'pages/{url_path}.html', f'pages/{url_path}/index.html']:
        try:
            get_template(template_name)
            return render(request, template_name)
        except TemplateDoesNotExist:
            continue
    raise Http404
