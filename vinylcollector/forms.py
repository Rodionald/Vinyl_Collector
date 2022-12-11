from django import forms
from vinylcollector.models import Vinyl


class VinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = ('artist', 'album', 'genres', 'styles', 'notes', 'formats', 'qty', 'manufacture_region', 'label',
                  'catalogue_number', 'year', 'average_rating', 'owners', 'sell', 'lowest_price', 'image',
                  'created_date')
