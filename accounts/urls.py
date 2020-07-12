from django.urls import path
from .views import register, logout_request
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    #path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('logout/', logout_request, name='logout_now'),
]
