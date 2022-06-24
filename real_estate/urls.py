from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('api/v1/profile/', include("apps.profiles.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to the Real Estate Portal"