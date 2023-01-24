from django.urls import path, include
from api.views import *

urlpatterns = [
    path('vinyls/', VinylDetailsView.as_view()),
    path('vinyls/<int:id>', VinylDetailsView.as_view()),
]