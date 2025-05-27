from django.urls import path
from .views import planet_list_view, planet_create_view, planet_update_view, planet_delete_view


urlpatterns = [
        path('list/', planet_list_view), 
        path('detail/<slug:slug>', planet_list_view),
        path('create/', planet_create_view), 
        path('edit/<slug:slug>', planet_update_view),
        path('delete/<slug:slug>', planet_delete_view),
        ]
