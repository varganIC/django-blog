from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('reg/', views.register, name='reg-page'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('profile/', views.profile, name='profile'),
    path('accounts/login/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
]
