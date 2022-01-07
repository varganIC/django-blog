from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('contacts', views.contact, name='contact-page'),
    path('uslugi', views.uslugi, name='uslugi-page'),
    path('news', views.ShowNewsView.as_view(), name='news-page'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/add', views.NewsCreateView.as_view(), name='news-add'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('news/user/<str:username>', views.UserALLNewsView.as_view(), name='user-news'),
]
