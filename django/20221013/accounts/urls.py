
from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
    path('login/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('<int:pk>/update/', views.update, name='update'),
    path('password/', views.password, name='password'),
    path('delete/', views.delete, name='delete'),
]