from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('vinylcollector_admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('vinylcollector.urls')),
    path('', include('django.contrib.auth.urls')),
)
