from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:code>/', views.redirect_url, name="redirect_url"),
    path('api/create/', views.api_create_short_url, name="api_create_short_url"),
]