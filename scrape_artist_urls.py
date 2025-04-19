from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from scrape_album_urls import *
from init_driver import *


def getArtistUrl(driver, artist_name):
    search_url = "https://music.youtube.com/search?q=" + artist_name

    driver.get(search_url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".card-container")),
    )
    print("search loaded")

    xpath = "//span[contains(@class, 'yt-formatted-string')][text() = 'Artist']/ancestor::div[contains(@class, 'metadata-container')]"
    artist_element = driver.find_element(By.XPATH, xpath)
    artist_url = artist_element.find_element(By.CSS_SELECTOR ,"a[href]").get_attribute("href")

    print(artist_url)
    return artist_url

def scrapeArists(artists):
    yt_music_url = "https://music.youtube.com"

    driver = initDriver(yt_music_url)
    
    artist_urls = []
    for artist in artists:  
        artist_urls.append(getArtistUrl(driver, artist))

    for artist_url in artist_urls:
        scrapeAlbumUrls(driver, artist_url)

artists = ["testament", "megadeth", "metallica"]
scrapeArists(artists)
