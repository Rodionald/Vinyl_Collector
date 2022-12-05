from django.urls import path
from vinylcollector.views import *

urlpatterns = [
    path('', hello_world),
    path('search/<str:vendor_code>', VinylView.vinyl_detail, name='search'),
    path('vinyl_detail', VinylView.vinyl_detail, name='detail')
]
