from django.urls import path
from articles import views

app_name = 'articles'

urlpatterns = [
    path('<int:num>', views.index, name='index'),
    path('<int:pk>/create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]