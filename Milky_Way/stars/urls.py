from django.urls import path
from .views import star_list_view, star_create_view, star_update_view, star_delete_view

urlpatterns = [
        path('list/', star_list_view),
        path('create/', star_create_view),
        path('update/<slug:slug>', star_update_view),
        path('detail/<slug:slug>', star_list_view),
        path('delete/<slug:slug>', star_delete_view),
        ]
