from django.db import models
from django.contrib.auth.models import User


class Vinyl(models.Model):
    release = models.CharField(max_length=24, verbose_name='Release Discogs')
    artist = models.CharField(max_length=80, verbose_name='Artist')
    album = models.CharField(max_length=80, verbose_name='Album')
    genres = models.CharField(max_length=80, verbose_name='Genres')
    styles = models.CharField(max_length=80, verbose_name='Styles')
    notes = models.TextField(verbose_name='Notes')
    formats = models.CharField(max_length=24, verbose_name='Formats')
    qty = models.CharField(max_length=8, verbose_name='Qty')
    manufacture_region = models.CharField(max_length=80, verbose_name='Manufacture region')
    label = models.CharField(max_length=80, verbose_name='Label')
    catalogue_number = models.CharField(max_length=80, verbose_name='Catalogue number')
    year = models.CharField(max_length=80, verbose_name='Year')
    average_rating = models.CharField(max_length=80, verbose_name='Average rating')
    owners_number = models.CharField(max_length=80, verbose_name='Owners')
    sell_number = models.CharField(max_length=80, verbose_name='Sell')
    lowest_price = models.CharField(max_length=80, verbose_name='Lowest price, USD')
    image = models.ImageField(verbose_name='Image', null=True, blank=True)
    image_url = models.CharField(max_length=255, verbose_name='Image URL', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Added to collection')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.catalogue_number}'


