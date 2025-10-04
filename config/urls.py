"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tracker.views import daily_summary, register, LoginView, profile_setup, edit_food, delete_food, edit_profile
from django.contrib.auth import views as auth_views
from tracker.forms import LoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tracker/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path("profile_setup/", profile_setup, name="profile_setup"),
    path('profile/', edit_profile, name='edit_profile'),
    path('', daily_summary, name='home'),
    path("edit_food/", edit_food, name="edit_food"),
    path("delete_food/", delete_food, name="delete_food"),
]
