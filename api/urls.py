from django.urls import path, include
from api.views import *

urlpatterns = [
    path('vinyls/', VinylList.as_view()),
    path('vinyls//', VinylDetail.as_view()),
]