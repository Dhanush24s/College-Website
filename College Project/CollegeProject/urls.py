from django.contrib import admin
from django.urls import path, include
from Backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('Backend/',include('Backend.urls')),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'), 
     
    

]
