from django.urls import path
from articles import views

urlpatterns = [
    path("", views.root),
    path("create/", views.create),
]
