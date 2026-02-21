from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/', views.site_search, name='search'),
    path('contact/send/', views.contact_page, name='contact'),
    path('admissions/apply-bachelor/', views.apply_bachelor_page, name='apply_bachelor'),
    path('admissions/apply-master/', views.apply_master_page, name='apply_master'),
    path('admissions/tuition-fees/', views.tuition_fees_page, name='tuition_fees'),
    path('admissions/scholarships/', views.scholarships_page, name='scholarships'),
    path('admissions/scholarships/<slug:slug>/', views.scholarship_detail, name='scholarship_detail'),
    path('careers/hiring/', views.hiring_page, name='hiring'),
    path('careers/hiring/<slug:slug>/', views.job_detail, name='job_detail'),
    path('<path:url_path>/', views.static_page, name='static_page'),
]
