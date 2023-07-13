
from django.contrib import admin
from django.urls import path,include 

from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),

    path('authentication/', include('user_control.urls')),
    path('frontend/', include('frontend.urls')),
    path('backend/', include('backend.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
