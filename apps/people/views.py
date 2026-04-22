from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext as _
from .models import Leader, Person
from apps.programs.models import Department, Program
from apps.news.models import NewsArticle, Event


def person_list(request):
    return render(request, 'pages/faculty/index.html')


def leadership(request):
    rektorat = Leader.objects.filter(category='rektorat')
    departament = Leader.objects.filter(category='departament')
    return render(request, 'pages/about/leadership.html', {
        'rektorat': rektorat,
        'departament': departament,
    })


def person_directory(request):
    people = Person.objects.select_related('department').prefetch_related('publications').all()
    departments = Department.objects.all()
    job_titles = (
        Person.objects.values_list('job_title', flat=True)
        .distinct()
        .order_by('job_title')
    )

    return render(request, 'pages/faculty/directory.html', {
        'people': people,
        'departments': departments,
        'job_titles': job_titles,
    })


def person_detail(request, slug):
    person = get_object_or_404(Person, slug=slug)
    return render(request, 'people/person_detail.html', {
        'person': person,
        'hero_title': person.full_name,
        'hero_category': person.t('job_title'),
        'breadcrumbs': [
            {'title': _('Faculty'), 'url': reverse('people:person_list')},
            {'title': person.full_name, 'url': None},
        ],
    })


def dept_jurisprudence(request):
    departments = Department.objects.filter(faculty='jurisprudence')
    programs = Program.objects.filter(is_published=True, faculty='jurisprudence').select_related('department')
    news = NewsArticle.objects.filter(is_published=True, faculty='jurisprudence')[:3]
    from django.utils import timezone
    _today = timezone.now().date()
    _ev = Event.objects.filter(is_published=True, faculty='jurisprudence')
    events = (list(_ev.filter(event_date__gte=_today).order_by('event_date')) + list(_ev.filter(event_date__lt=_today).order_by('-event_date')))[:3]
    return render(request, 'pages/faculty/jurisprudence.html', {
        'departments': departments,
        'programs': programs,
        'news': news,
        'events': events,
    })


def dept_business_innovative(request):
    departments = Department.objects.filter(faculty='business')
    programs = Program.objects.filter(is_published=True, faculty='business').select_related('department')
    news = NewsArticle.objects.filter(is_published=True, faculty='business')[:3]
    from django.utils import timezone
    _today = timezone.now().date()
    _ev = Event.objects.filter(is_published=True, faculty='business')
    events = (list(_ev.filter(event_date__gte=_today).order_by('event_date')) + list(_ev.filter(event_date__lt=_today).order_by('-event_date')))[:3]
    return render(request, 'pages/faculty/business-innovative-education.html', {
        'departments': departments,
        'programs': programs,
        'news': news,
        'events': events,
    })
