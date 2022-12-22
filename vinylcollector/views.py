from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View
from vinylcollector.models import Vinyl
from vinyl.vinyl import *
from vinylcollector.forms import VinylForm
from django.contrib.auth.models import User


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
        Vinyl.objects.create('owner')
        return render(request, 'vinylcollector/successfully_added.html')


class VinylAddView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        form = VinylForm()
        return render(request, 'vinylcollector/add_vinyl.html', {'form': form})

    @staticmethod
    def post(request, *args, **kwargs):
        vinyl = Vinyl.save(request)
        return render(request, 'details_vinyl.html', vinyl)


class UserVinylCollectionView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        vinyls = Vinyl.objects.all()
        paginator = Paginator(vinyls, 8)
        page = request.GET.get('page')
        try:
            vinyls = paginator.page(page)
        except PageNotAnInteger:
            vinyls = paginator.page(1)
        except EmptyPage:
            vinyls = paginator.page(paginator.num_pages)
        return render(request, 'vinylcollector/my_collection.html', {'vinyls': vinyls})

    @staticmethod
    def post(request, *args, **kwargs):
        vinyl = Vinyl.objects.filter()
        return render(request, 'vinylcollector/my_collection.html', {'vinyl': vinyl})
