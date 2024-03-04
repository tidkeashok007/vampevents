from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('make-me-groom/', views.makeme_groom, name='make-me-groom'),
    path('make-me-bride/', views.makeme_bride, name='make-me-bride'),
    path('costume-groom/', views.costume_groom, name='costume-groom'),
    path('costume-bride/', views.costume_bride, name='costume-bride'),
    path('decorations-indoor/', views.decorations_indoor, name='decorations-indoor'),
    path('decorations-outdoor/', views.decorations_indoor, name='decorations-outdoor'),
    path('mehendi/', views.mehendi, name='mehendi'),
    path('party-space/', views.party_space, name='party-space'),
    path('capture-me/', views.capture_me, name='capture-me'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)