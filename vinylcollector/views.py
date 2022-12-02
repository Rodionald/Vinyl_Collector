from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from vinylcollector.models import Vinyl
from vinylcollector.forms import VinylForm


def hello_world():
    return HttpResponse('Hello World!!!')


class VinylView(View):

    pass

    # def vinyl_list(request):
    #     vinyls = Vinyl.objects.all()
    #     return render(request, 'vinylcollector/vinyl_list.html', {'vinyls': vinyls})
    #
    # def vinyl_add(request):
    #     form = VinylForm
    #     return render(request, 'vinylcollector/vinyl_add.html', {'form': form})
