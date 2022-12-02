from vinyl.vinyl import Vinyl

'''The goal of this app is collect info about Vinyl LP you have in your collection and have opportunity share info
about yours collection with friends via social networks '''

if __name__ == '__main__':
    vinyl = input('Input vendor code \n')
    print(Vinyl(vinyl).dict())
