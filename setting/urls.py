
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('admin/', admin.site.urls),
    # url reload tailwind
    path("__reload__/", include("django_browser_reload.urls")),
    
    path('', include('core.urls')),
    path('', include('school.urls')),
    path('', include('classe.urls')),
    path('', include('student.urls')),
    path('', include('badge.urls')),

    # users
    path('', include('users.urls')),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)