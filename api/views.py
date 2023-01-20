from rest_framework import generics
from . import serializers
from .models import Vinyl


class VinylList(generics.ListCreateAPIView):
    queryset = Vinyl.objects.all()
    serializer_class = serializers.VinylSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VinylDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vinyl.objects.all()
    serializer_class = serializers.VinylSerializer
