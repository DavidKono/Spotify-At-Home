import os

aritsts_dir = "downloaded_content/artists"

def getArtistDirectoryName(artist_name):
    artist_path = os.path.join(aritsts_dir, artist_name)
    artist_path = os.path.normpath(artist_path)
    return artist_path

def makeArtistDirectory(artist_name):
    artist_path = getArtistDirectoryName(artist_name)

    if (not os.path.exists(artist_path)):
        os.mkdir(artist_path)

def getAlbumDirectoryName(artist_name, album_name):
    artist_path = getArtistDirectoryName(artist_name)

    album_path = os.path.join(artist_path, album_name)
    album_path = os.path.normpath(album_path)
    return album_path

def makeAlbumDirectory(artist_name, album_name):
    album_path = getAlbumDirectoryName(artist_name, album_name)

    if (not os.path.exists(album_path)):
        os.makedirs(album_path)
