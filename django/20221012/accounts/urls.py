from . import views
from django.urls import path
app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
    path('login/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
]