from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View
from vinylcollector.models import Vinyl
from vinyl.vinyl import *
from vinylcollector.forms import *


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
        vinyl_dict = eval(request.POST.get('context'))
        vinyl = Vinyl(**vinyl_dict)
        vinyl.owner = request.user
        vinyl.save()
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
        form = VinylForm()
        return render(request, 'vinylcollector/add_vinyl.html', {'form': form})

    @staticmethod
    def post(request, *args, **kwargs):
        vinyl = Vinyl()
        vinyl.release = request.POST.get("release")
        vinyl.artist = request.POST.get("artist")
        vinyl.album = request.POST.get("album")
        vinyl.genres = request.POST.get("genres")
        vinyl.styles = request.POST.get("styles")
        vinyl.notes = request.POST.get("notes")
        vinyl.formats = request.POST.get("formats")
        vinyl.qty = request.POST.get("qty")
        vinyl.manufacture_region = request.POST.get("manufacture_region")
        vinyl.label = request.POST.get("label")
        vinyl.catalogue_number = request.POST.get("catalogue_number")
        vinyl.year = request.POST.get("year")
        vinyl.image_url = request.POST.get("image_url")
        vinyl.owner = request.user
        vinyl.save()
        return render(request, 'vinylcollector/successfully_added.html')


class UserVinylCollectionView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        vinyls = Vinyl.objects.filter(owner=request.user)
        paginator = Paginator(vinyls, 12)
        page = request.GET.get('page')
        try:
            vinyls = paginator.page(page)
        except PageNotAnInteger:
            vinyls = paginator.page(1)
        except EmptyPage:
            vinyls = paginator.page(paginator.num_pages)
        return render(request, 'vinylcollector/my_collection.html', {'page': page, 'vinyls': vinyls})

    @staticmethod
    def post(request, *args, **kwargs):
        vinyl = Vinyl.objects.filter()
        return render(request, 'vinylcollector/my_collection.html', {'vinyl': vinyl})
