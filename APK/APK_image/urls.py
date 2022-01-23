
from django.urls import path
from APK_image.views import index, filter_violations
from django.conf.urls.static import static
from django.conf import settings # new

urlpatterns = [
    path('', index, name='index'),
    path('<int:gas_pipeline_pk>/', filter_violations, name='filter_violations'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
