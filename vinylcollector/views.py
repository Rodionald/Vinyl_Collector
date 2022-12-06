from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
# from vinylcollector.models import Vinyl
from vinyl.vinyl import Vinyl
from vinylcollector.forms import VinylForm


def hello_world(request):
    return HttpResponse('Hello World')


class VinylView(View):

    def vinyl_search(self):
        return render(self, 'vinylcollector/vinyl_search.html')

    def vinyl_detail(self, vendor_code):
        vinyl = Vinyl(vendor_code)
        context = vinyl.dict
        return render(self, 'vinylcollector/vinyl_detail.html', {'context': context})
