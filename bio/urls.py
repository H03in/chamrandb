from django.urls import path
from bio import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about')
]
