from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('blogs', views.blogs ),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy)
]