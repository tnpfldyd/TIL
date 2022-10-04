from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.board, name='board'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
