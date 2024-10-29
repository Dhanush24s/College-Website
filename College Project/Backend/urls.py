from django.contrib import admin
from django.urls import path
from Backend import views

urlpatterns = [
     
    path('home/', views.HomePage, name='home'),
    path('about/', views.AboutPage, name='about'),
    path('contact/', views.ContactPage, name='contact'),
    path('course/', views.CoursePage, name='course'),
    path('single/', views.SinglePage, name='single'),
    path('teacher/', views.TeacherPage, name='teacher'),    
    path('joinnow/', views.JoinnowPage, name='joinnow'),  
]


