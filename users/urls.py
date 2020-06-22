from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/', login_page, name="login_page_url"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout_page.html'), name="logout_page_url"),
    path('register/', register_page, name="register_page_url"),
]
