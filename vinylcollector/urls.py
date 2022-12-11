from django.urls import path
from vinylcollector.views import *

urlpatterns = [
    path('', VinylView.vinyl_search, name='main'),
    path('search/vendor_code', VinylView.vinyl_detail, name='search_vinyl'),
    path('search', VinylView.vinyl_search, name='search'),
]
