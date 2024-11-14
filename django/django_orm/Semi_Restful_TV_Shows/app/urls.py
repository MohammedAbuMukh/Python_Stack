from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.addShow),
    path('shows/create', views.createShow),
    path('shows/<int:id>', views.showID),
    path('shows/<int:id>/destroy', views.deleteShow),
    path('show/<int:id>/edit', views.editshow, name="edit"),
    path('confirmedit', views.update)
]