import requests
import re
import json

'''Get the id of LP you have.
NOTICE! For Russian LP, vendor code types in Russian language!!!
Get the Info about searching LP, such as Artist, Album, Country, Year, Average price of this LP, etc'''


class DiscogsSite:

    def __init__(self, request: str):
        self.request = request.replace(' ', '')
        self.search_type = 'all'

    def get_release(self) -> int:
        try:
            url = f'https://www.discogs.com/search?q={self.request}&type={self.search_type}'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/107.0.0.0 Safari/537.36 ',
            }
            response = requests.get(url, headers=headers).text
            release = re.findall(r'<a.+?href="/release/(.+?)-.+?"', response)[1]
        except IndexError:
            release = 'Wrong vendor code'
        return release


class SearchingData:
    def __init__(self, release: int | None):
        self.release = release
        self.json_data = None

    def get_json_data(self) -> dict:
        try:
            url = f'https://api.discogs.com/releases/{self.release}'
            data = requests.get(url)
            self.json_data = json.loads(data.content.decode())
        except TypeError:
            self.json_data = 'Wrong vendor code'
        return self.json_data


class Vinyl_Lp:
    def __init__(self, json_data: dict | None):
        self.json_data = json_data

    @property
    def release(self) -> str:
        release = self.json_data.get('id', 'not specified')
        return release

    @property
    def artist(self) -> str:
        artist = self.json_data.get('artists_sort', 'not specified')
        return artist

    @property
    def album(self) -> str:
        album = self.json_data.get('title', 'not specified')
        return album

    @property
    def genres(self) -> str:
        genres = ''.join(self.json_data.get('genres', 'not specified'))
        return genres

    @property
    def styles(self) -> str:
        styles = ''.join(self.json_data.get('styles', 'not specified'))
        return styles

    @property
    def country(self) -> str:
        country = self.json_data.get('country', 'not specified')
        return country

    @property
    def year(self) -> int:
        year = self.json_data.get('year', 'not specified')
        return year

    @property
    def average_rating(self) -> float:
        try:
            rating = self.json_data['community']['rating']['average']
        except KeyError:
            rating = 0.0
        return rating

    @property
    def owners_number(self) -> int:
        owners = self.json_data.get('community', {'have': 0}).get('have', 0)
        return owners

    @property
    def sell_number(self) -> int:
        sell = self.json_data.get('num_for_sale', 0)
        return sell

    @property
    def lowest_price(self) -> float:
        lowest_price = self.json_data.get('lowest_price', 0.0)
        return lowest_price

    @property
    def notes(self) -> str:
        notes = self.json_data.get('notes', 'not specified').replace('\n', ' ')
        return notes

    @property
    def formats(self):
        try:
            formats = self.json_data.get('formats')[0].get('name', 'not specified')
        except TypeError:
            formats = 'not specified'
        return formats

    @property
    def qty(self) -> str:
        try:
            qty = self.json_data.get('formats')[0].get('qty', 'not specified')
        except TypeError:
            qty = 'not specified'
        return qty

    @property
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

    @property
    def label(self) -> str:
        try:
            label = self.json_data.get('labels')[0].get('name', 'not specified')
        except TypeError:
            label = 'not specified'
        return label

    @property
    def cat_num(self) -> str:
        try:
            cat_num = self.json_data.get('labels')[0].get('catno', 'not specified')
        except TypeError:
            cat_num = 'not specified'
        return cat_num

    @property
    def dict(self) -> dict:
        vinyl = {
            'release': self.release,
            'artist': self.artist,
            'album': self.album,
            'genres': self.genres,
            'styles': self.styles,
            'notes': self.notes,
            'formats': self.formats,
            'qty': self.qty,
            'manufacture_region': self.country,
            'label': self.label,
            'catalogue_number': self.cat_num,
            'year': self.year,
            'average_rating': self.average_rating,
            'owners': self.owners_number,
            'sell': self.sell_number,
            'lowest_price': self.lowest_price,
            'image_url': self.image_url,
        }
        return vinyl

