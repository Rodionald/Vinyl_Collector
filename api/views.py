from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from vinylcollector.models import Vinyl, UserData
from .serializers import UserSerializer, VinylSerializer


class UserList(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class VinylListView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        vinyls = Vinyl.objects.all()
        serializer = VinylSerializer(vinyls, many=True)
        return Response({"vinyls": serializer.data})


class VinylDetailsView(APIView):

    @staticmethod
    def get(request, pk):
        vinyls = Vinyl.objects.filter(pk=pk)
        serializer = VinylSerializer(vinyls, many=True)
        return Response({"vinyls": serializer.data})

    @staticmethod
    def post(request, pk):
        vinyl = request.data.get('vinyls')
        serializer = VinylSerializer(data=vinyl)
        if serializer.is_valid(raise_exception=True):
            vinyl_saved = serializer.save()
            return Response({"success": f"Vinyl with catalogue number:'{vinyl_saved.catalogue_number}' created "
                                        f"successfully"})

    @staticmethod
    def put(request, pk):
        saved_vinyl = generics.get_object_or_404(Vinyl.objects.all(), pk=pk)
        data = request.data.get('vinyls')
        serializer = VinylSerializer(instance=saved_vinyl, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            vinyl_saved = serializer.create(data)
            return Response({
                "success": f"Vinyl with catalogue number:'{vinyl_saved.catalogue_number}' updated successfully",
            })

    @staticmethod
    def delete(request, pk):
        vinyl = generics.get_object_or_404(Vinyl, pk=pk)
        vinyl.delete()
        return Response({
            "message": f"Vinyl with catalogue number:'{vinyl.catalogue_number}' has been deleted."
        },)

