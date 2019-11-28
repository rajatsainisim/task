from django.conf.urls.static import static
from django.urls import path


from app import views
from task import settings

urlpatterns = [
    path('', views.homea, name='homea'),
    path('index/', views.index, name='index'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
