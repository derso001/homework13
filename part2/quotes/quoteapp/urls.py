from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('quote/', views.quote, name='quote'),
    path('tag/', views.tag, name='tag'),
    path('author/', views.author, name='author'),
    path('<str:author>', views.detail_author, name='detail_author'),
    path('tag/<str:tag_name>/', views.quotes_by_tag, name='quotes_by_tag'),
]