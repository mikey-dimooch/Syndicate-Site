from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path('tour/', views.tour, name='tour'),
    path('band/', views.band, name='band'),
    path('music/', views.music, name='music'),
    path('merch/', views.merch, name='merch'),
    path('contact/', views.contact, name='contact'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)