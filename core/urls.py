from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

api_root_url = 'api/v1/'


urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_root_url + 'token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path(api_root_url + 'token/refresh/',
         jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path(api_root_url, include('api.urls')),
    path('tinymce/', include('tinymce.urls')),
]
