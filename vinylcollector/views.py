from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum, Count
from django.shortcuts import render, get_object_or_404
from django.views import View
from vinyl.vinyl import *
from vinylcollector.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


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
        message = 'message'
        return render(request, 'vinylcollector/search_vinyl.html', {'message': message})


class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class VinylFromCollectionView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        if request.GET.get('vinyl_id'):
            vinyl_id = request.GET.get('vinyl_id')
            vinyl = get_object_or_404(Vinyl, id=vinyl_id)
            return render(request, 'vinylcollector/details_vinyl_from_collection.html', {'vinyl': vinyl})
        return render(request, 'vinylcollector/my_collection.html')


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
        vinyl.user_rating = request.POST.get("user_rating")
        vinyl.save()
        message = 'message'
        return render(request, 'vinylcollector/search_vinyl.html', {'message': message})


class UserVinylCollectionView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        vinyls = Vinyl.objects.filter(owner=request.user).values('id', 'artist', 'album', 'image_url',
                                                                 'lowest_price')
        aggregated_data = vinyls.aggregate(total_coast=Sum('lowest_price'), total_count=Count('id'))
        qty_vinyl = aggregated_data['total_count']
        if qty_vinyl == 0:
            return render(request, 'vinylcollector/empty_collection.html')
        else:
            try:
                total_coast = round(aggregated_data['total_coast'], 2)
            except TypeError:
                total_coast = 0
            paginator = Paginator(vinyls, 12)
            page = request.GET.get('page')
            try:
                vinyls = paginator.page(page)
            except PageNotAnInteger:
                vinyls = paginator.page(1)
            except EmptyPage:
                vinyls = paginator.page(paginator.num_pages)
            return render(request, 'vinylcollector/my_collection.html',
                          {'page': page, 'vinyls': vinyls, 'qty_vinyl': qty_vinyl, 'total_coast': total_coast})

