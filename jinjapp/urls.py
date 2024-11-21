
from django.urls import path
from jinjapp import views


urlpatterns=[
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts,name='contacts'),
    path('services/', views.services, name='services'),


]