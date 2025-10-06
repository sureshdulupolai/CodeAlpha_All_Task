from django.urls import path
from . import views

app_name = 'jobapp'

urlpatterns = [
    # Candidate Views
    path('list/', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('<int:job_id>/apply/', views.apply_job, name='apply_job'),

    # Employer Views
    path('add/', views.add_job, name='add_job'),
    path('post/', views.post_job, name='post_job'),
]
