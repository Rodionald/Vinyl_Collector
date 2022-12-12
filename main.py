from vinyl.vinyl import *

'''The goal of this app is collect info about Vinyl LP you have in your collection and have opportunity share info
about yours collection with friends via social networks '''

if __name__ == '__main__':
    vendor_code = input('Input vendor code \n')
    search = DiscogsSite(vendor_code)
    release = search.get_release()
    searching_data = SearchingData(release)
    json_data = SearchingData.get_json_data(searching_data)
    vinyl = Vinyl(json_data)
    vinyl_info = vinyl.dict
    print(vinyl_info)
