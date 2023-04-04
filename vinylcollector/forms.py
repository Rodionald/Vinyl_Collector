from django.forms import ModelForm
from vinylcollector.models import Vinyl


class VinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = '__all__'


class DiscogsVinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = '__all__'
