from django.urls import path
from .views import home, about, programs, contact, news_list, admission, boarding, why

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('programs/', programs, name='programs'),
    path('contact/', contact, name='contact'),
    path('news/', news_list, name='news_list'),
    path('admission/', admission, name='admissions'),
    path('boarding/', boarding, name='boarding_details'),
    path('why-choose-us/', why, name='why_spia'),
]
