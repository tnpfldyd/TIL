"""day3pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from practices import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index),
    path("is_odd_even/<name>", views.is_odd_even),
    path("calculate/<num1>/<num2>", views.calculate),
    path("time_machine/", views.time_machine),
    path("hangle_index/", views.hangle_index),
    path("hangle/", views.hangle),
]
