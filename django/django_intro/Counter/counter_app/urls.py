from django.urls import *     
from . import views
urlpatterns = [
    path('', views.index),     
    path('destroy_session', views.destroy_session),
    path('increment_by_2',views.increment_by_2),
    path('reset',views.reset)
    
]