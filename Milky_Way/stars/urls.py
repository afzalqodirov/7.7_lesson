from django.urls import path
from .views import star_list_view, star_create_view

urlpatterns = [
        path('list/', star_list_view),
        path('create/', star_create_view),
        ]
