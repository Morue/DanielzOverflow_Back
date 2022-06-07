"""danielzoverflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('jwtauth.urls')),
    # default path => list of questions
    path('', RedirectView.as_view(url='api/questions/')),
    path('questions/', include('question.urls')),
    path('profiles/', include('user_profile.urls')),
    path('tags/', include('tag.urls')),
    # API urls
    path('api/', RedirectView.as_view(url='questions/')),
    path('api/questions/', include('question.api-urls')),
    path('api/profiles/', include('user_profile.api-urls')),
    path('api/tags/', include('tag.api-urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
