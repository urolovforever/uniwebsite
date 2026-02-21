from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext as _
from .models import Person
from apps.programs.models import Department, Program


def person_list(request):
    return render(request, 'pages/faculty/index.html')


def person_directory(request):
    people = Person.objects.select_related('department').all()
    departments = Department.objects.all()

    return render(request, 'pages/faculty/directory.html', {
        'people': people,
        'departments': departments,
    })


def person_detail(request, slug):
    person = get_object_or_404(Person, slug=slug)
    return render(request, 'people/person_detail.html', {
        'person': person,
        'hero_title': person.full_name,
        'hero_category': person.get_role_display(),
        'breadcrumbs': [
            {'title': _('Faculty'), 'url': reverse('people:person_list')},
            {'title': person.full_name, 'url': None},
        ],
    })


def dept_jurisprudence(request):
    """Faculty of Jurisprudence detail page."""
    programs = Program.objects.filter(
        is_published=True,
        department__slug='jurisprudence',
    ).select_related('department')
    return render(request, 'pages/faculty/jurisprudence.html', {
        'programs': programs,
    })


def dept_business_innovative(request):
    """Faculty of Business and Innovative Education detail page."""
    programs = Program.objects.filter(
        is_published=True,
        department__slug='business-innovative-education',
    ).select_related('department')
    return render(request, 'pages/faculty/business-innovative-education.html', {
        'programs': programs,
    })
