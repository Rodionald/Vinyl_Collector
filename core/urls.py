
from django.contrib import admin
from django.urls import path, include
from vinylcollector.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world()),
    path('vinyl', include('vinylcollector.urls'))
]
