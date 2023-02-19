from django.urls import path, include
from api.views import *

urlpatterns = [
    path('vinyls/', VinylListView.as_view()),
    path('vinyls/<int:pk>', VinylDetailsView.as_view()),
]