from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext as _
from .models import Department, Program


def program_list(request, level=None):
    programs = Program.objects.filter(is_published=True).select_related('department')
    title = _('All Programs')
    if level:
        programs = programs.filter(level=level)
        if level == 'phd':
            title = _('PhD Programs')
        elif level == 'master':
            title = _("Master's Programs")
        else:
            title = _("Bachelor's Programs")

    departments = Department.objects.all()

    return render(request, 'programs/program_list.html', {
        'programs': programs,
        'departments': departments,
        'current_level': level,
        'hero_title': title,
        'hero_category': _('Academic Programs'),
        'breadcrumbs': [
            {'title': _('Programs'), 'url': reverse('programs:program_list') if level else None},
            {'title': title, 'url': None} if level else None,
        ],
    })


def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug, is_published=True)
    related_programs = Program.objects.filter(
        is_published=True, level=program.level,
    ).select_related('department').exclude(pk=program.pk)[:5]
    return render(request, 'programs/program_detail.html', {
        'program': program,
        'related_programs': related_programs,
        'hero_title': program.t('title'),
        'hero_category': f'{program.get_level_display()} {_("Programme")}',
        'hero_description': f'{program.department.t("name")} · {program.get_study_type_display()}',
        'breadcrumbs': [
            {'title': _('Programs'), 'url': reverse('programs:program_list')},
            {'title': f"{program.get_level_display()}'s", 'url': reverse('programs:program_list') + f'{program.level}/'},
            {'title': program.t('title'), 'url': None},
        ],
    })


def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug)
    programs = department.programs.filter(is_published=True)
    return render(request, 'programs/department_detail.html', {
        'department': department,
        'programs': programs,
        'hero_title': department.t('name'),
        'hero_category': _('Departments'),
        'breadcrumbs': [
            {'title': _('Programs'), 'url': reverse('programs:program_list')},
            {'title': department.t('name'), 'url': None},
        ],
    })


def by_faculty_page(request):
    """Programs by Faculty page with dynamic programme tags."""
    jurisprudence_programs = Program.objects.filter(
        is_published=True, department__slug='jurisprudence',
    ).select_related('department')
    business_programs = Program.objects.filter(
        is_published=True, department__slug='business-innovative-education',
    ).select_related('department')
    return render(request, 'pages/programs/by-faculty.html', {
        'jurisprudence_programs': jurisprudence_programs,
        'business_programs': business_programs,
    })


def by_level_page(request):
    """Programs by Level page with dynamic programme cards."""
    bachelor_programs = Program.objects.filter(is_published=True, level='bachelor').select_related('department')
    master_programs = Program.objects.filter(is_published=True, level='master').select_related('department')
    phd_programs = Program.objects.filter(is_published=True, level='phd').select_related('department')
    return render(request, 'pages/programs/by-level.html', {
        'bachelor_programs': bachelor_programs,
        'master_programs': master_programs,
        'phd_programs': phd_programs,
    })
