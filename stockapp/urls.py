from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homeview, name= 'home'),
    path('signin', views.signinpage,name='signin'),
    path('login', LoginView.as_view(template_name='stockapp/login.html'),name='login'),
    path('logout', LogoutView.as_view()),
    path('trade', views.trade, name='trade'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

