from vinyl.vinyl import *

'''The goal of this app is collect info about Vinyl LP you have in your collection and have opportunity share info
about yours collection with friends via social networks '''

if __name__ == '__main__':
    art = get_vendor_code()
    vinyl_id = get_id(art)
    js = get_js(vinyl_id)
    vinyl = get_vinyl_dict(js)
    print(vinyl)
