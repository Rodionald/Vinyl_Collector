from django.forms import ModelForm
from vinylcollector.models import Vinyl


class VinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = ["artist", "album", "genres", "notes", "formats", "qty", "image", "user_rating"]


class DiscogsVinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = '__all__'
