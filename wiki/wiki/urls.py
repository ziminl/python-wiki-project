from django.urls import path
from articles import views

urlpatterns = [
    path('wiki/', views.article_list, name='wiki'),
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_new, name='article_new'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
]