from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.SignupView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='homepage/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),

]



