from django.shortcuts import render
from django.views import View
from vinylcollector.models import Vinyl
from vinyl.vinyl import *
from vinylcollector.forms import VinylForm


class MainPage(View):

    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'vinylcollector/main.html')


class Search(View):

    @staticmethod
    def get(request, *args, **kwargs):
        vendor_code = request.GET.get('vendor_code')
        if vendor_code:
            vinyl = VinylView.get(request)
            return vinyl
        return render(request, 'vinylcollector/search_vinyl.html')

    @staticmethod
    def post(request, *args, **kwargs):
        return render(request, 'vinylcollector/successfully_added.html')


class VinylView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        vendor_code = request.GET.get('vendor_code')
        discogs_search = DiscogsSite(vendor_code)
        release = discogs_search.get_release()
        searching_data = SearchingData(release)
        vinyl_json_data = searching_data.get_json_data()
        vinyl = Vinyl_Lp(vinyl_json_data)
        context = vinyl.dict
        return render(request, 'vinylcollector/details_vinyl.html', {'context': context})

    @staticmethod
    def post(request, *args, **kwargs):
        return render(request, 'vinylcollector/successfully_added.html')


class VinylAddView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'vinylcollector/add_vinyl.html')

    @staticmethod
    def post(request, *args, **kwargs):
        form = VinylForm
        context = {
            'form': form
        }
        return render(request, 'details_vinyl.html', context)


class UserVinylCollectionView(View):
    paginated_by = 20

    def get(request, Vinyl, *args, **kwargs):
        vinyl = Vinyl.objects.all()
        return render(request, 'my_collection.html', {'vinyl': vinyl})

