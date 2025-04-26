from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def scrapeAlbumUrls(driver, artist_url):

    driver.get(artist_url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content-wrapper")),
    )
    print("content loaded")

    albums_div = driver.find_element(By.XPATH, '//a[text()="Albums"]/ancestor::div[contains(@class, "content-group")]')
    print("found albums section")
    albums_button = WebDriverWait(albums_div, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[.//span[text()='More']]"))
    )
    try: 
        albums_button.click()
    except Exception as e: 
        print("couldnt go to albums")
        print("error: ", e)
        driver.quit()
        exit()

    print("went to albums section")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ytmusic-grid-renderer")),
    )
    print("albums loaded")

    album_titles = []
    album_urls = []
    
    albums_div = driver.find_element(By.CSS_SELECTOR, "#items.ytmusic-grid-renderer")
    albums = albums_div.find_elements(By.CSS_SELECTOR, ".ytmusic-grid-renderer")
    print("found albums")
    for album in albums:
        try:
            album_details = album.find_element(By.CLASS_NAME, "title")
            album_title = album_details.text
            album_url = album_details.find_element(By.TAG_NAME, "a").get_attribute("href")

            album_titles.append(album_title)
            album_urls.append(album_url)
            
        except Exception as e: 
            print(f"couldnt get album details for {album}")
            print("error: ", e)

    for album in album_titles:
        print(album)
    return album_titles, album_urls

