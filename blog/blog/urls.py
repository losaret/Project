"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from blog_site.views import Index
from user_profile.views import Register
from blog_site import views as blog_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('register/', Register, name='Register'),
    path('user/<str:username>/', blog_site.Profile.as_view()),
    path('post/', blog_site.Publishpost.as_view()),
    path('hashtag/<str:hashtag>/', blog_site.HastagCloud.as_view()),
    path('search/', blog_site.Search.as_view())
]
