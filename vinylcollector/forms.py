from django.forms import ModelForm
from vinylcollector.models import Vinyl


class VinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = ('artist', 'album', 'genres', 'styles', 'notes', 'formats', 'qty', 'manufacture_region', 'label',
                  'catalogue_number', 'year', 'image_url')


class DiscogsVinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = (
            'release', 'artist', 'album', 'genres', 'styles', 'notes', 'formats', 'qty', 'manufacture_region', 'label',
            'catalogue_number', 'year', 'average_rating', 'owners_number', 'sell_number', 'lowest_price', 'image',
            'image_url')
