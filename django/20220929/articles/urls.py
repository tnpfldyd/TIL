from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('', views.root, name='root'),
    path('main/<int:num>', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('create2/', views.create2, name="create2"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('edti2/<int:pk>', views.edit2, name='edit2'),
    path('delete/<int:pk>', views.delete, name="delete"),
]