from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum, Count
from django.shortcuts import render, get_object_or_404
from django.views import View
from core.settings.base import TG_TOKEN, TG_CHAT_ID
from vinyl.vinyl import *
from vinylcollector.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests


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

    @staticmethod
    def post(request, *args, **kwargs):
        """star rating"""
        pass


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


class VinylSellView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        if request.GET.get('vinyl_id'):
            vinyl_id = request.GET.get('vinyl_id')
            vinyl = get_object_or_404(Vinyl, id=vinyl_id)
            return render(request, 'vinylcollector/sell_vinyl.html', {'vinyl': vinyl})
        return render(request, 'vinylcollector/main.html')

    @staticmethod
    def post(request, *args, **kwargs):
        vinyl_img = request.POST.get('vinyl_img')
        vinyl_artist = request.POST.get('vinyl_artist')
        vinyl_album = request.POST.get('vinyl_album')
        vinyl_price = request.POST.get('vinyl_price')
        vinyl_formats = request.POST.get('vinyl_formats')
        vinyl_qty = request.POST.get('vinyl_qty')
        vinyl_manufacture_region = request.POST.get('vinyl_manufacture_region')
        vinyl_year = request.POST.get('vinyl_year')
        sell_city = request.POST.get('sell_city')
        sell_price = request.POST.get('sell_price')
        sell_contact = request.POST.get('sell_contact')
        sell_condition = request.POST.get('sell_condition')
        sell_contact_info = request.POST.get('sell_contact_info')
        description = f'Исполнитель: <b>{vinyl_artist}</b>\nАльбом: <b>{vinyl_album}</b>\nФормат издания (' \
                      f'количество): <b>{vinyl_formats} ({vinyl_qty})</b>\nРегион про' \
                      f'изводства: <b>{vinyl_manufacture_region}</b>\nГод издания: <b>{vinyl_year}</b>\nНаименьшая ' \
                      f'цена в интернете, $: <b>{vinyl_price}</b>\nСостояние: <b>{sell_condition}</b>\nЦена продавца, ' \
                      f'BYN: <b>{sell_price}</b>\nГород продажи: <b>{sell_city}</b>\nКонтактная информация: <b>' \
                      f'{sell_contact_info} {sell_contact}</b> '
        url = f'https://api.telegram.org/bot{TG_TOKEN}/sendPhoto?chat_id={TG_CHAT_ID}&photo={vinyl_img}' \
              f'&caption={description}&parse_mode=HTML'
        print(requests.get(url).json())
        message = 'sell'
        vinyl_id = request.POST.get('vinyl_id')
        vinyl = get_object_or_404(Vinyl, id=vinyl_id)
        return render(request, 'vinylcollector/details_vinyl_from_collection.html', {'vinyl': vinyl, 'message': message})


class VinylEditView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        if request.GET.get('vinyl_id'):
            vinyl_id = request.GET.get('vinyl_id')
            vinyl = get_object_or_404(Vinyl, id=vinyl_id)
            return render(request, 'vinylcollector/edit_vinyl.html', {'vinyl': vinyl})
        return render(request, 'vinylcollector/main.html')

    @staticmethod
    def post(request, *args, **kwargs):
        vinyl_notes = request.POST.get('vinyl_notes')
        vinyl_id = request.POST.get('vinyl_id')
        vinyl = get_object_or_404(Vinyl, id=vinyl_id)
        vinyl.notes = vinyl_notes
        vinyl.save()
        message = 'edit'
        return render(request, 'vinylcollector/details_vinyl_from_collection.html', {'vinyl': vinyl, 'message': message})


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

