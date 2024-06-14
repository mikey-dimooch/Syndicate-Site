from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import contact
from .views import album_details  # Import the correct view function


urlpatterns = [
    path("", views.home, name="home"),
    path('tour/', views.tour, name='tour'),
    path('band/', views.band, name='band'),
    path('music/', views.music, name='music'),
    path('merch/', views.merch, name='merch'),
    path('contact/', views.contact, name='contact'),
    path('albums/<int:id>/', views.album_details, name='album-details'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)