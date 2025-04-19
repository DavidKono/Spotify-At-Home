from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from scrape_artist import *
from reject_cookies import * 

yt_music_url = "https://music.youtube.com"

options = Options()
# options.add_argument('--headless=new')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

def getArtistUrl(artist_name):
    search_url = "https://music.youtube.com/search?q=" + artist_name

    driver.get(search_url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".card-container")),
    )
    print("search loaded")

    # artist_element = driver.find_element(By.CSS_SELECTOR, ".style-scope.yt-formatted-string")
    # xpath = "//span[contains(@class, 'yt-formatted-string')][text() = 'Artist']"
    xpath = "//span[contains(@class, 'yt-formatted-string')][text() = 'Artist']/ancestor::div[contains(@class, 'metadata-container')]"
    artist_element = driver.find_element(By.XPATH, xpath)
    artist_url = artist_element.find_element(By.CSS_SELECTOR ,"a[href]").get_attribute("href")
    # artist_element = driver.find_element(By.XPATH, "//yt-formatted-string[contains(text(), 'Artist')]/ancestor::div[contains(@class, 'metadata-container')]")
    # artist_url = artist_element.find_element(By.TAG_NAME, "a").get_attribute("href")
    # <a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="channel/UCAzb0gYKjvUm-WNy-tevEcw">Testament</a>

    print(artist_url)
    return artist_url


def scrapeArists(artists):
    rejectCookies()
    
    artist_urls = []
    for artist in artists:  
        artist_urls.append(getArtistUrl(artist))

    # for artist_url in artist_urls:
    #     scrapeArtist(artist_url)

    scrapeArtist("https://music.youtube.com/channel/UCGexNm_Kw4rdQjLxmpb2EKw")
        

artists = ["testament", "megadeth", "metallica"]
scrapeArists(artists)

# artist_urls = []
# for artist in artists:
#     artist_urls.append(getArtistUrl(artist))

# https://music.youtube.com/search?q=testament