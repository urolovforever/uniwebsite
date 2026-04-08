from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('directory/', views.person_directory, name='person_directory'),
    path('jurisprudence/', views.dept_jurisprudence, name='dept_jurisprudence'),
    path('business-innovative-education/', views.dept_business_innovative, name='dept_business_innovative'),
    path('<slug:slug>/', views.person_detail, name='person_detail'),
]
