from django import forms
from vinylcollector.models import Vinyl


class VinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = (
            'release',
        )
