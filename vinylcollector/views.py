from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
# from vinylcollector.models import Vinyl
from vinyl.vinyl import *

from vinylcollector.forms import VinylForm


def hello_world(request):
    return HttpResponse('Hello World')


class VinylView(View):

    def vinyl_detail(self, vendor_code):
        vinyl = Vinyl(vendor_code)
        context = vinyl.dict()
        return render(self, 'vinylcollector/vinyl_detail.html', {'context': context})

    def vinyl_info(self, vendor_code):
        context = vinyl_dict(vendor_code)
        return render(self, 'vinylcollector/vinyl_detail.html', {'context': context})
