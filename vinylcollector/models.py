from django.db import models
from django.contrib.auth.models import User


class Vinyl(models.Model):
    release = models.CharField(max_length=24, verbose_name='Release Discogs', null=True, blank=True)
    artist = models.CharField(max_length=80, verbose_name='Artist')
    album = models.CharField(max_length=80, verbose_name='Album')
    genres = models.CharField(max_length=80, verbose_name='Genres', null=True, blank=True)
    styles = models.CharField(max_length=80, verbose_name='Styles', null=True, blank=True)
    notes = models.TextField(verbose_name='Notes', null=True, blank=True)
    formats = models.CharField(max_length=24, verbose_name='Formats', null=True, blank=True)
    qty = models.CharField(max_length=8, verbose_name='Qty', null=True, blank=True)
    manufacture_region = models.CharField(max_length=80, verbose_name='Manufacture region')
    label = models.CharField(max_length=80, verbose_name='Label')
    catalogue_number = models.CharField(max_length=80, verbose_name='Catalogue number', null=True, blank=True)
    year = models.CharField(max_length=80, verbose_name='Year')
    average_rating = models.CharField(max_length=80, verbose_name='Average rating', null=True, blank=True)
    owners_number = models.DecimalField(max_digits=80, decimal_places=0, verbose_name='Owners', null=True, blank=True)
    sell_number = models.DecimalField(max_digits=80, decimal_places=0, verbose_name='Sell', null=True, blank=True)
    lowest_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Lowest price, USD', null=True,
                                       blank=True)
    image = models.ImageField(verbose_name='Image', null=True, blank=True)
    image_url = models.CharField(max_length=255, verbose_name='Image URL', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Added to collection')
    # refreshing_date = models.DateField(auto_now_add=True, verbose_name='Date of refreshing')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    user_rating = models.CharField(max_length=2, verbose_name='User rating', null=True, blank=True)

    def __str__(self):
        return f'{self.catalogue_number}'
