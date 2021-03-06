from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', TemplateView.as_view(template_name='registration\home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]