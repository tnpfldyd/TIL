
from django.urls import path
from movies import views
app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]