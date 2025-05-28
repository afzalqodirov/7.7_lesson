from django.urls import path
from .views import register_view, users_view

urlpatterns = [
        path('register/', register_view),
        path('users/', users_view),
        ]
