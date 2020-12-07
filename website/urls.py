from django.urls import path

from . import views

urlpatterns = [
    path('^$', views.home, name="home"),
    path('service/', views.service, name="service"),
]