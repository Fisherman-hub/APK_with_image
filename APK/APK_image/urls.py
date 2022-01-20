
from django.urls import path
from APK_image.views import index

urlpatterns = [
    path('', index, name='index'),
]
