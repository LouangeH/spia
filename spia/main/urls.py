from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('programs/', programs, name='programs'),
    path('contact/', contact, name='contact'),
    path('news/', news_list, name='news_list'),
    path('admission_online/', register_student, name='admissions'),
    path('admission/', admission, name='admissions_presentation'),    
    path('governance/', governance, name='governance'),
    path('courses/', courses, name='courses'),
    path('boarding/', boarding, name='boarding_details'),
    path('tenders/', tender_list, name='tender_list'),
    path('tenders/create/', tender_create, name='tender_create'),
    path('tenders/edit/<int:pk>/', tender_edit, name='tender_edit'),
    path('tenders/delete/<int:pk>/', tender_delete, name='tender_delete'),

    path('spia_admin/login/', admin_login, name='admin_login'),
    path('spia_admin/register/', admin_register, name='admin_register'),
    path('spia_admin/logout/', admin_logout, name='admin_logout'),
    path('spia_admin/dashboard/', admin_dashboard, name='admin_dashboard'),

    path('news/create/', news_create, name='news_create'),
    path('news/<int:pk>/edit/', news_edit, name='news_edit'),
    path('news/<int:pk>/delete/', news_delete, name='news_delete'),

    #path
]
