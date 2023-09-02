"""
URL configuration for cook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

# Define urls to the food app and the django admin page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
]

# Add a functionality to the patterns as to allow for the images in django database to be retrieved
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
