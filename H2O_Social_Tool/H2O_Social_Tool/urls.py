"""H2O_Social_Tool URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from H2O_Social_Tool import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('H2O_Portal/', include('django.contrib.auth.urls')),
    #url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    path('', include('H2O_Portal.urls')),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
