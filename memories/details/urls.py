from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('memory/<int:memory_id>', views.detail, name='detail'),
    path('memory/<int:memory_id>/delete',views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
