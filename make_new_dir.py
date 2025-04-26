import os
import json

artists_dir = "downloaded_content/artists"
albums_json_name = "albums.json"
artists_json_name = "artists.json"

def getArtistDirectoryName(artist_name):
    artist_path = os.path.join(artists_dir, artist_name)
    artist_path = os.path.normpath(artist_path)
    return artist_path

def makeArtistDirectory(artist_name):
    artist_path = getArtistDirectoryName(artist_name)

    if (not os.path.exists(artist_path)):
        os.makedirs(artist_path)
 
def appendAlbumToJson(artist_name, album_name):
    artist_path = getArtistDirectoryName(artist_name)
    json_path = os.path.join(artist_path, albums_json_name)

    if not os.path.exists(json_path):
        with open(json_path, "w") as f:
            json.dump([], f)

    with open(json_path, "r+") as f:
        file_data = json.load(f)
        if album_name not in file_data:
            file_data.append(album_name)
            f.seek(0)
            json.dump(file_data, f)
            f.truncate()
        else:
            print(f"album {album_name} from artist {artist_name} already in json")

def appendArtistToJson(artist_name, album_name):
    artist_path = getArtistDirectoryName(artist_name)
    json_path = os.path.join(artist_path, artists_json_name)

    if not os.path.exists(json_path):
        with open(json_path, "w") as f:
            json.dump([], f)

    with open(json_path, "r+") as f:
        file_data = json.load(f)
        if album_name not in file_data:
            file_data.append(album_name)
            f.seek(0)
            json.dump(file_data, f)
            f.truncate()
        else:
            print(f"artist {artist_name} already in json")

# def createArtistJson(artist_path):
#     json_path = os.path.join(artist_path, json_name)
#     if not os.path.exists(json_path):
#         json_file = open(json_path, "x")


# def createArtistJson(artist_path):
#     existing_albums = os.listdir(artist_path)

#     json_path = os.path.join(artist_path, json_name)
#     if not os.path.exists(json_path):
#         json_file = open(json_path, "x")


def getAlbumDirectoryName(artist_name, album_name):
    artist_path = getArtistDirectoryName(artist_name)

    album_path = os.path.join(artist_path, album_name)
    album_path = os.path.normpath(album_path)
    return album_path

def makeAlbumDirectory(artist_name, album_name):
    album_path = getAlbumDirectoryName(artist_name, album_name)

    if (not os.path.exists(album_path)):
        os.makedirs(album_path)

