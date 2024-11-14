from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_book',views.add_book, name='add_book'),
    path('view_book/<int:id>', views.view_book, name='view_book'),
    # path('add_dojo/', views.add_dojo, name='add_dojo'),
    # path('add_ninja/', views.add_ninja, name='add_ninja'),
    # path('delete_dojo/<int:dojo_id>/', views.delete_dojo, name='delete_dojo'),
]
