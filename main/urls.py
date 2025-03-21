from django.contrib import admin
from django.urls import path, include
from home import views 
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'home.views.not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  
    path('packages/', include('packages.urls')),  
         
 
]


# media file handling
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)