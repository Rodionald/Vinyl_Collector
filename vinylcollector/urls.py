from django.urls import path
from vinylcollector.views import *


urlpatterns = [
    path('', vinyl_list),
]
