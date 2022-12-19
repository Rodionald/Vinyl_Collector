from django.urls import path, include
from django.contrib.auth.urls import *
from vinylcollector.views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('search', Search.as_view(), name='search'),
    path('search/', VinylView.as_view(), name='vinyl_details'),
    path('add', VinylAddView.as_view(), name='vinyl_add'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
