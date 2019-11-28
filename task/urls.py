from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('app/', include('django.contrib.auth.urls')),

]
