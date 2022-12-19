from django.forms import ModelForm,TextInput,Textarea
from vinylcollector.models import *


class VinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = ('artist', 'album', 'genres', 'styles', 'notes', 'formats', 'qty', 'manufacture_region', 'label',
                  'catalogue_number', 'year', 'image')
        widgets = {
            'artist': TextInput(attrs={
                'class': 'form-control'
            }),
            'album': TextInput(attrs={
                'class': 'form-control',
            })
        }


