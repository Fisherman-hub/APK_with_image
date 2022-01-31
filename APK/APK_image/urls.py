
from django.urls import path
from APK_image.views import Index, Filter_Violations
from APK_image.views import ViolationFormView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:gas_pipeline_pk>/', Filter_Violations.as_view(), name='filter_violations'),
    path('add_violation/', ViolationFormView.as_view(), name='add_violation'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
