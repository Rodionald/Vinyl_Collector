
from django.contrib import admin
from django.urls import path, include
from vinylcollector.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vinylcollector.urls')),
    path('', include('api.urls')),
]
