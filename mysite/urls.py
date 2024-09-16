"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import HomeIncluding another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.global_settings import MEDIA_URL
from django.contrib import admin
from django.urls import path,include
from myapp import views
from . import settings
from django.conf.urls.static import static
#588. Creating Superuser
#A super user is some user which actually has access to all of your website and he can control and manipulate
#therefore he must actually have all the privileges to add data, remove data, modify data or view data.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
