from yt_dlp import YoutubeDL

from init_driver import *
from scrape_artist_urls import *
from make_new_dir import *

def scrapeAristsWithSearch(artists):
    yt_music_url = "https://music.youtube.com"

    driver = initDriver(yt_music_url)
    
    for artist in artists:  
        artist_urls = []

        try:
            artist_urls.append(getArtistUrl(driver, artist))
        except Exception as e: 
            print(f"Couldnt get artist {artist}")
            print("error: ", e)

        for artist_url in artist_urls:
            scrapeArtist(driver, artist, artist_url)

def scrapeAristsWithUrls(artists, artist_urls):
    yt_music_url = "https://music.youtube.com"

    driver = initDriver(yt_music_url)
    
    for i in range(len(artists)):
        scrapeArtist(driver, artists[i], artist_urls[i])
        
def scrapeArtist(driver, artist, artist_url):
    try: 
        album_titles, album_urls = scrapeAlbumUrls(driver, artist_url)
        makeArtistDirectory(artist)
        appendArtistToJson(artist)

        for i in range(len(album_titles)):
            downloadAlbum(artist, album_titles[i], album_urls[i])

    except Exception as e: 
        print(f"failed to download albums from {artist}")
        print("error: ", e)

def downloadPlaylist(playlist_url, playlist_title):
    
    makeArtistDirectory("Misc_Playlists")
    appendArtistToJson("Misc_Playlists")

    if getAlbumAlreadyExists("Misc_Playlists", playlist_title):
        print(f"Playlist {playlist_title} already downloaded")
        return
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_audio': True,
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
        'noplaylist': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Change to 'm4a', 'wav', etc. if needed
            'preferredquality': '192',
        }],
    }  

    try: 
        album_dir = getAlbumDirectoryName("Misc_Playlists", playlist_title)
        album_dir_option = {'outtmpl': f"{album_dir}/%(title)s.%(ext)s"}

        ydl_opts = {**ydl_opts, **album_dir_option}

        with YoutubeDL(ydl_opts) as ytdl:
            ytdl.download(playlist_url)

        appendAlbumToJson("Misc_Playlists", playlist_title)

    except Exception as e: 
        print(f"failed to scrape Playlist {playlist_title}")
        print("error: ", e)



        

def downloadAlbum(artist, album, album_url):
    if getAlbumAlreadyExists(artist, album):
        print(f"Album {album} by artist {artist} already downloaded")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_audio': True,
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
        'noplaylist': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Change to 'm4a', 'wav', etc. if needed
            'preferredquality': '192',
        }],
    }  

    try: 
        album_dir = getAlbumDirectoryName(artist, album)
        album_dir_option = {'outtmpl': f"{album_dir}/%(title)s.%(ext)s"}

        ydl_opts = {**ydl_opts, **album_dir_option}

        with YoutubeDL(ydl_opts) as ytdl:
            ytdl.download(album_url)

        appendAlbumToJson(artist, album)

    except Exception as e: 
        print(f"failed to scrape album {album} from {artist}")
        print("error: ", e)
