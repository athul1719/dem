from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('about',views.about),
    path('news',views.news),
    path('contact',views.contact),
]