import requests
import re
import json

'''Get the id of LP you have.
NOTICE! For Russian LP, vendor code types in Russian language!!!
Get the Info about searching LP, such as Artist, Album, Country, Year, Average price of this LP, etc'''


class Vinyl:
    def __init__(self, vendor_code: str):
        self.vendor_code = vendor_code.replace(' ', '')

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

    def js(self) -> dict:
        try:
            js_url = f'https://api.discogs.com/releases/{self.release()}'
            data = requests.get(js_url)
            js = json.loads(data.content.decode())
        except TypeError:
            js = 'Wrong vendor code'
        return js

    def url(self):
        try:
            url = self.js()['uri']
        except KeyError:
            url = 'Wrong vendor code'
        return url

    def artist(self) -> str:
        try:
            artist = self.js()['artists_sort']
        except KeyError:
            artist = 'Wrong vendor code'
        return artist

    def album(self) -> str:
        try:
            album = self.js()['title']
        except KeyError:
            album = 'not specified'
        return album

    def genres(self) -> str:
        try:
            genres = ''.join(self.js()['genres'])
        except KeyError:
            genres = 'not specified'
        return genres

    def styles(self) -> str:
        try:
            styles = ''.join(self.js()['styles'])
        except KeyError:
            styles = 'not specified'
        return styles

    def country(self) -> str:
        try:
            country = self.js()['country']
        except KeyError:
            country = 'not specified'
        return country

    def year(self) -> int:
        try:
            year = self.js()['year']
        except KeyError:
            year = 'not specified'
        return year

    def average_rating(self) -> float:
        try:
            rating = self.js()['community']['rating']['average']
        except KeyError:
            rating = 0.0
        return rating

    def owners_number(self) -> int:
        try:
            owners = self.js()['community']['have']
        except KeyError:
            owners = 0
        return owners

    def sell_number(self) -> int:
        try:
            sell = self.js()['num_for_sale']
        except KeyError:
            sell = 0
        return sell

    def lowest_price(self) -> float:
        try:
            lowest_price = self.js()['lowest_price']
            if lowest_price is None:
                lowest_price = 0.0
        except KeyError:
            lowest_price = 0.0
        return lowest_price

    def notes(self) -> str:
        try:
            notes = self.js()['notes'].replace('\n', ' ')
        except KeyError:
            notes = 'not specified'
        return notes

    def formats(self):
        try:
            formats = self.js()['formats'][0]['name']
        except KeyError:
            formats = 'not specified'
        return formats

    def qty(self) -> str:
        try:
            qty = self.js()['formats'][0]['qty']
        except KeyError:
            qty = 'not specified'
        return qty

    def image_url(self) -> str:
        try:
            url = f'https://www.discogs.com/release/{self.js()["id"]}'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8, '
                          'application/signed-exchange;v=b3;q=0.9',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/107.0.0.0 Safari/537.36 ',
            }
            response = requests.get(url, headers=headers).text
            image_url = re.findall(r'id="release_schema".+?"image":"(.+?)"', response)[0]
        except KeyError:
            image_url = 'No image url'
        return image_url

    def label(self) -> str:
        try:
            label = self.js()['labels'][0]['name']
        except KeyError:
            label = 'not specified'
        return label

    def cat_num(self) -> str:
        try:
            cat_num = self.js()['labels'][0]['catno']
        except KeyError:
            cat_num = 'not specified'
        return cat_num

    def dict(self) -> dict:
        vinyl = {
            'release': self.release(),
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


def get_release(vendor_code) -> str:
    try:
        url = f'https://www.discogs.com/search?q={vendor_code}&type=all'
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


def get_js(vendor_code) -> dict:
    try:
        js_url = f'https://api.discogs.com/releases/{get_release(vendor_code)}'
        data = requests.get(js_url)
        js = json.loads(data.content.decode())
    except TypeError:
        js = 'Wrong vendor code'
    return js


def get_url(js):
    try:
        url = js['uri']
    except KeyError:
        url = 'Wrong vendor code'
    return url


def get_artist(js) -> str:
    try:
        artist = js['artists_sort']
    except KeyError:
        artist = 'Wrong vendor code'
    return artist


def get_album(js) -> str:
    try:
        album = js['title']
    except KeyError:
        album = 'not specified'
    return album


def get_genres(js) -> str:
    try:
        genres = ''.join(js['genres'])
    except KeyError:
        genres = 'not specified'
    return genres


def get_styles(js) -> str:
    try:
        styles = ''.join(js['styles'])
    except KeyError:
        styles = 'not specified'
    return styles


def get_country(js) -> str:
    try:
        country = js['country']
    except KeyError:
        country = 'not specified'
    return country


def get_year(js) -> int:
    try:
        year = js['year']
    except KeyError:
        year = 'not specified'
    return year


def get_average_rating(js) -> float:
    try:
        rating = js['community']['rating']['average']
    except KeyError:
        rating = 0.0
    return rating


def get_owners_number(js) -> int:
    try:
        owners = js['community']['have']
    except KeyError:
        owners = 0
    return owners


def get_sell_number(js) -> int:
    try:
        sell = js['num_for_sale']
    except KeyError:
        sell = 0
    return sell


def get_lowest_price(js) -> float:
    try:
        lowest_price = js['lowest_price']
        if lowest_price is None:
            lowest_price = 0.0
    except KeyError:
        lowest_price = 0.0
    return lowest_price


def get_notes(js) -> str:
    try:
        notes = js['notes'].replace('\n', ' ')
    except KeyError:
        notes = 'not specified'
    return notes


def get_formats(js):
    try:
        formats = js['formats'][0]['name']
    except KeyError:
        formats = 'not specified'
    return formats


def get_qty(js) -> str:
    try:
        qty = js['formats'][0]['qty']
    except KeyError:
        qty = 'not specified'
    return qty


def get_image_url(js) -> str:
    try:
        url = f'https://www.discogs.com/release/{js["id"]}'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8, '
                      'application/signed-exchange;v=b3;q=0.9',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/107.0.0.0 Safari/537.36 ',
        }
        response = requests.get(url, headers=headers).text
        image_url = re.findall(r'id="release_schema".+?"image":"(.+?)"', response)[0]
    except KeyError:
        image_url = 'No image url'
    return image_url


def get_label(js) -> str:
    try:
        label = js['labels'][0]['name']
    except KeyError:
        label = 'not specified'
    return label


def get_cat_num(js) -> str:
    try:
        cat_num = js['labels'][0]['catno']
    except KeyError:
        cat_num = 'not specified'
    return cat_num


def vinyl_dict(vendor_code) -> dict:
    js = get_js(vendor_code)
    vinyl = {
        'release': get_release(vendor_code),
        'artist': get_artist(js),
        'album': get_album(js),
        'genres': get_genres(js),
        'styles': get_styles(js),
        'notes': get_notes(js),
        'formats': get_formats(js),
        'qty': get_qty(js),
        'manufacture_region': get_country(js),
        'label': get_label(js),
        'catalogue_number': get_cat_num(js),
        'year': get_year(js),
        'average_rating': get_average_rating(js),
        'owners': get_owners_number(js),
        'sell': get_sell_number(js),
        'lowest_price': get_lowest_price(js),
        'image': get_image_url(js),
    }
    return vinyl
