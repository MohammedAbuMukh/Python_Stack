from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_course, name='add_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
]