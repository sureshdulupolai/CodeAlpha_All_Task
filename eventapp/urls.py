from django.urls import path
from . import views

app_name = 'eventapp'

urlpatterns = [
    path('list/', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/register/', views.register_event, name='register_event'),
    path('api/list/', views.api_event_list, name='api_event_list'),
]
