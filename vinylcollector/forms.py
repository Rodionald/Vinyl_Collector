from django.forms import ModelForm
from vinylcollector.models import Vinyl


class VinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = ('artist', 'album', 'genres', 'styles', 'notes', 'formats', 'qty', 'manufacture_region', 'label',
                  'catalogue_number', 'year', 'image_url')

