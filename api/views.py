from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vinyl
from .serializers import VinylSerializer


class VinylDetailsView(APIView):

    @staticmethod
    def get(request):
        vinyls = Vinyl.objects.all()
        serializer = VinylSerializer(vinyls, many=True)
        return Response({"vinyls": serializer.data})

    @staticmethod
    def post(request):
        vinyl = request.data.get('vinyls')
        serializer = VinylSerializer(data=vinyl)
        if serializer.is_valid(raise_exception=True):
            vinyl_saved = serializer.save()
        return Response({"success": "Vinyl '{}' created successfully".format(vinyl_saved.catalogue_number)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(Vinyl.objects.all(), pk=pk)
        data = request.data.get('vinyls')
        serializer = VinylSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            vinyl_saved = serializer.save()
        return Response({
            "success": "Vinyl '{}' updated successfully".format(vinyl_saved.title),
        })

    @staticmethod
    def delete(request, pk):
        article = get_object_or_404(Vinyl.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Vinyl with id `{}` has been deleted.".format(pk)
        }, status=204)
