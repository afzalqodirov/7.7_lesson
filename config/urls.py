from django.contrib import admin
from django.urls import path, include

#jwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#drf yasg ------ swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema = get_schema_view(openapi.Info(title='Just api', default_version='v0.-01'))

urlpatterns = [
        path('', schema.with_ui('swagger')),
        path('admin/', admin.site.urls),
        path('planets/', include('Milky_Way.planets.urls')),
        path('stars/', include('Milky_Way.stars.urls')),
]
