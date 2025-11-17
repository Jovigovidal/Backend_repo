# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.get_user_data, name='get_user_data'),
]