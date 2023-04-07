from django.urls import path
from vinylcollector.views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('my_collection', UserVinylCollectionView.as_view(), name='my_collection'),
    path('my_collection/', VinylFromCollectionView.as_view(), name='vinyl_from_collection_details'),
    path('search', Search.as_view(), name='search'),
    path('registration', SignUpView.as_view(), name='registration'),
    path('search/', VinylView.as_view(), name='vinyl_details'),
    path('add', VinylAddView.as_view(), name='vinyl_add'),
]
