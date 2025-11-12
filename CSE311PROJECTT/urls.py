from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # zoomda bahsettiğim hazır giriş/çıkış sistemi, django direkt sağlıyor ayarları da settings.py dan yönetebiliyoruz
    path('accounts/', include('django.contrib.auth.urls')),

    # app URL si
    path('', include('course_management.urls')),
]

# geliştirme ortamında medya dosyaları için
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
