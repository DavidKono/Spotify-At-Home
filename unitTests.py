from yt_dlp import YoutubeDL

from init_driver import *
from scrape_artist_urls import *
from scrape_artists import *
from make_new_dir import *


yt_music_url = "https://music.youtube.com"

# artist_url = "https://music.youtube.com/channel/UC0HijtVThn8Y_iUdVjEI6Ww"
artist_url = "https://music.youtube.com/channel/UCGexNm_Kw4rdQjLxmpb2EKw"
artists = ["metallica"]
artist = "metallica"
album = "ride the lightening"
album_url = "https://music.youtube.com/playlist?list=OLAK5uy_nMi553Un-V3VCacIvHuLPUgXfEdPmHaP8"

def test_scrapeAlbums():
    driver = initDriver(yt_music_url)
    scrapeAlbumUrls(driver, artist_url)

def test_scrapeAristsWithSearch():
    scrapeAristsWithSearch(artists)

def test_downloadAlbum():
    downloadAlbum(artist, album, album_url)

# test_scrapeAlbums()
# test_scrapeAristsWithSearch()
test_downloadAlbum()


# appendAlbumToJson("testament", "jojo haha")


# artists = ["theocracy"]
# artist_urls = ["https://music.youtube.com/channel/UC0HijtVThn8Y_iUdVjEI6Ww"]
# scrapeAristsWithUrls(artists, artist_urls)