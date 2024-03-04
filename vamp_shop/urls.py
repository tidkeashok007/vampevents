from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact, name = 'ContactUs'),
    path('tracker/', views.tracker, name = 'TrackingStatus'),
    path('search/', views.search, name = 'Search'),
    path('products/<int:myid>', views.products, name = 'products'),
    path('checkout/', views.checkout, name = 'Checkout'),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
    path('login/', LoginView.as_view(template_name='shop/login.html'), name = 'login'),
    path('signup/', views.handlesignup, name="signup"),
    path('loginpost/', views.handlelogin, name="loginpost"),
    path('logout/', views.handleLogout, name="logout"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)