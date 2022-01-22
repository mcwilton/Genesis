from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Genesis import settings

admin.site.site_header = 'Genesis Admin'
admin.site.index_title = 'Genesis Self-paced Learning System'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('', include('accounts.urls')),
    path('', include('udemy.urls')),
    path('', include('courses.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
