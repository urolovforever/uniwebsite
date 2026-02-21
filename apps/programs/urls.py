from django.urls import path
from . import views
from apps.core.views import static_page

app_name = 'programs'

urlpatterns = [
    path('', views.program_list, name='program_list'),
    path('bachelor/', views.program_list, {'level': 'bachelor'}, name='bachelor_list'),
    path('master/', views.program_list, {'level': 'master'}, name='master_list'),
    path('phd/', views.program_list, {'level': 'phd'}, name='phd_list'),
    path('by-faculty/', views.by_faculty_page, name='by_faculty'),
    path('by-level/', views.by_level_page, name='by_level'),
    path('department/<slug:slug>/', views.department_detail, name='department_detail'),
    # Static sub-pages (joint-degrees, exchange-programs, dual-diploma)
    path('joint-degrees/', static_page, {'url_path': 'programs/joint-degrees'}, name='joint_degrees'),
    path('exchange-programs/', static_page, {'url_path': 'programs/exchange-programs'}, name='exchange_programs'),
    path('dual-diploma/', static_page, {'url_path': 'programs/dual-diploma'}, name='dual_diploma'),
    path('<slug:slug>/', views.program_detail, name='program_detail'),
]
