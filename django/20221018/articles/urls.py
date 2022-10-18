from django.urls import path
from . import views
# Create your views here.

app_name = 'articles'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:pk>/',views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/comments/', views.comments, name='comments'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]