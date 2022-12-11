from django.shortcuts import render
from django.views import View
from vinylcollector.models import Vinyl
from vinyl.vinyl import Vinyl


class VinylView(View):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.GET = None

    def vinyl_search(self):
        return render(self, 'vinylcollector/vinyl_search.html')

    def vinyl_detail(self):
        vendor_code = self.GET.get('vendor_code', None)
        vinyl = Vinyl(vendor_code)
        context = vinyl.dict
        return render(self, 'vinylcollector/vinyl_detail.html', {'context': context})
