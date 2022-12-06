import requests
import re
import json

'''Get the id of LP you have.
NOTICE! For Russian LP, vendor code types in Russian language!!!
Get the Info about searching LP, such as Artist, Album, Country, Year, Average price of this LP, etc'''


class Vinyl:
    def __init__(self, vendor_code: str):
        self.vendor_code = vendor_code.replace(' ', '')
        self.release = self.release()
        self.js = self.js()

    def release(self) -> str:
        try:
            url = f'https://www.discogs.com/search?q={self.vendor_code}&type=all'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/107.0.0.0 Safari/537.36 ',
            }
            response = requests.get(url, headers=headers).text
            vinyl_release = re.findall(r'<a.+?href="/release/(.+?)-.+?"', response)[1]
        except IndexError:
            vinyl_release = 'Wrong vendor code'
        return vinyl_release

    def js(self):
        try:
            js_url = f'https://api.discogs.com/releases/{self.release}'
            data = requests.get(js_url)
            self.js = json.loads(data.content.decode())
        except TypeError:
            self.js = 'Wrong vendor code'
        return self.js

    def url(self):
        url = self.js.get('uri', 'not specified')
        return url

    def artist(self) -> str:
        artist = self.js.get('artists_sort', 'not specified')
        return artist

    def album(self) -> str:
        album = self.js.get('title', 'not specified')
        return album

    def genres(self) -> str:
        genres = ''.join(self.js.get('genres', 'not specified'))
        return genres

    def styles(self) -> str:
        styles = ''.join(self.js.get('styles', 'not specified'))
        return styles

    def country(self) -> str:
        country = self.js.get('country', 'not specified')
        return country

    def year(self) -> int:
        year = self.js.get('year', 'not specified')
        return year

    def average_rating(self) -> float:
        try:
            rating = self.js['community']['rating']['average']
        except KeyError:
            rating = 0.0
        return rating

    def owners_number(self) -> int:
        owners = self.js.get('community', {'have': 0}).get('have', 0)
        return owners

    def sell_number(self) -> int:
        sell = self.js.get('num_for_sale', 0)
        return sell

    def lowest_price(self) -> float:
        lowest_price = self.js.get('lowest_price', 0.0)
        return lowest_price

    def notes(self) -> str:
        notes = self.js.get('notes', 'not specified').replace('\n', ' ')
        return notes

    def formats(self):
        try:
            formats = self.js.get('formats')[0].get('name', 'not specified')
        except TypeError:
            formats = 'not specified'
        return formats

    def qty(self) -> str:
        try:
            qty = self.js.get('formats')[0].get('qty', 'not specified')
        except TypeError:
            qty = 'not specified'
        return qty

    def image_url(self) -> str:
        try:
            url = f'https://www.discogs.com/release/{self.release}'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8, '
                          'application/signed-exchange;v=b3;q=0.9',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/107.0.0.0 Safari/537.36 ',
            }
            response = requests.get(url, headers=headers).text
            image_url = re.findall(r'id="release_schema".+?"image":"(.+?)"', response)[0]
        except IndexError:
            image_url = 'https://cdn-icons-png.flaticon.com/512/6134/6134065.png'
        return image_url

    def label(self) -> str:
        try:
            label = self.js.get('labels')[0].get('name', 'not specified')
        except TypeError:
            label = 'not specified'
        return label

    def cat_num(self) -> str:
        try:
            cat_num = self.js.get('labels')[0].get('catno', 'not specified')
        except TypeError:
            cat_num = 'not specified'
        return cat_num

    def dict(self) -> dict:
        vinyl = {
            'release': self.release,
            'artist': self.artist(),
            'album': self.album(),
            'genres': self.genres(),
            'styles': self.styles(),
            'notes': self.notes(),
            'formats': self.formats(),
            'qty': self.qty(),
            'manufacture_region': self.country(),
            'label': self.label(),
            'catalogue_number': self.cat_num(),
            'year': self.year(),
            'average_rating': self.average_rating(),
            'owners': self.owners_number(),
            'sell': self.sell_number(),
            'lowest_price': self.lowest_price(),
            'image': self.image_url(),
        }
        return vinyl
