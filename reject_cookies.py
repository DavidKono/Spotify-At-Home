from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# first thing reject cookies on yt music
def rejectCookies(url):
    driver.get(url)

    try:
        reject_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button//span[text()='Reject all']"))
        )
        reject_button.click()
        print("rejected cookies")

    except TimeoutException:
        print("consent page didnt come up")
        driver.quit()
        exit()

    return driver